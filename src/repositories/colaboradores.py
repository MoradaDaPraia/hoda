from dtos.projeto import ProjetoDTO
from filters.colaborador import ColaboradorFilter
from dtos.colaborador import ColaboradorDTO
from exceptions.internal import InternalException
from repositories.repository import Repository


class ColaboradoresRepository(Repository):
    def __init__(self) -> None:
        super().__init__()

    def inserir_colaborador(
        self, nome: str, codinome: str, senha_hash: str
    ) -> ColaboradorDTO:
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO colaboradores (
                    nome, codinome, senha_hash
                ) VALUES ( ?, ?, ? );
                """,
                (nome, codinome, senha_hash),
            )
            id = cursor.lastrowid
            if id is None:
                raise InternalException("Não foi possível inserir o colaborador.")

            connection.commit()
            return ColaboradorDTO(id, nome, codinome, senha_hash)

    def consultar_colaborador_por_codinome(
        self, codinome: str
    ) -> ColaboradorDTO | None:
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    id, nome, codinome, senha_hash
                FROM colaboradores
                WHERE codinome = ?;
                """,
                (codinome,),
            )
            rows = cursor.fetchall()
            if len(rows) < 1:
                return None

            id, nome, codinome_retornado, senha_hash = rows[0]

            connection.commit()
            return ColaboradorDTO(id, nome, codinome_retornado, senha_hash)

    def listar_colaboradores_por_filtro(
        self, colaborador_filter: ColaboradorFilter
    ) -> list[ColaboradorDTO]:
        with self.connect() as connection:
            cursor = connection.cursor()

            query = """
                SELECT
                    c.id, c.nome, c.codinome, c.senha_hash
                FROM colaboradores c
                """
            params = []
            if colaborador_filter.projeto is not None:
                query += (
                    "INNER JOIN projetos_colaboradores pc ON pc.colaborador_id = c.id "
                )
            query += "WHERE 1 = 1 "
            if colaborador_filter.nome is not None:
                query += "AND LOWER(c.nome) LIKE LOWER(?) "
                params.append(f"%{colaborador_filter.nome}%")

            if colaborador_filter.projeto is not None:
                query += "AND pc.projeto_id = ? "
                params.append(colaborador_filter.projeto.id)

            query += ";"

            cursor.execute(query, tuple(params))
            rows = cursor.fetchall()

            colaboradores = []
            for row in rows:
                id, nome, codinome, senha_hash = row
                colaboradores.append(ColaboradorDTO(id, nome, codinome, senha_hash))

            connection.commit()
            return colaboradores
