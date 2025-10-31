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

            connection.commit()

    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect("./__data__/database.sqlite3")
