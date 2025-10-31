from dtos.projeto import ProjetoDTO
from exceptions.internal import InternalException
from repositories.repository import Repository


class ProjetosRepository(Repository):
    def __init__(self) -> None:
        super().__init__()

    def inserir_projeto(self, nome: str, codinome: str, descricao: str) -> ProjetoDTO:
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO projetos (
                    nome, codinome, descricao
                ) VALUES ( ?, ?, ? );
                """,
                (nome, codinome, descricao),
            )
            id = cursor.lastrowid
            if id is None:
                raise InternalException("Não foi possível inserir o projeto.")

            connection.commit()
            return ProjetoDTO(id, nome, codinome, descricao)

    def consultar_projeto_por_codinome(self, codinome: str) -> ProjetoDTO | None:
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    id, nome, codinome, descricao
                FROM projetos
                WHERE codinome = ?;
                """,
                (codinome,),
            )
            rows = cursor.fetchall()
            if len(rows) < 1:
                return None

            id, nome, codinome_retornado, descricao = rows[0]

            connection.commit()
            return ProjetoDTO(id, nome, codinome_retornado, descricao)
