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
