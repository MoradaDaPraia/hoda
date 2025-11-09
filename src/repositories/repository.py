from abc import ABC
import sqlite3


class Repository(ABC):
    def __init__(self) -> None:
        with sqlite3.connect("./__data__/database.sqlite3") as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS projetos (
                    id INTEGER NOT NULL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    codinome TEXT NOT NULL UNIQUE,
                    descricao TEXT NOT NULL
                );
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS colaboradores (
                    id INTEGER NOT NULL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    codinome TEXT NOT NULL,
                    senha_hash TEXT NOT NULL
                );
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS projetos_colaboradores (
                    id INTEGER NOT NULL PRIMARY KEY,
                    projeto_id INTEGER NOT NULL,
                    colaborador_id INTEGER NOT NULL,
                    FOREIGN KEY (projeto_id)
                        REFERENCES projetos (id)
                        ON DELETE CASCADE,
                    FOREIGN KEY (colaborador_id)
                        REFERENCES colaboradores (id)
                        ON DELETE CASCADE
                );
                """
            )

            connection.commit()

    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect("./__data__/database.sqlite3")
