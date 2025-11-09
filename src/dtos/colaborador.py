class ColaboradorDTO:
    def __init__(self, id: int, nome: str, codinome: str, senha_hash: str) -> None:
        self.id = id
        self.nome = nome
        self.codinome = codinome
        self.senha_hash = senha_hash

    def __str__(self) -> str:
        return f"""Colaborador
    Nome: {self.nome}
    Codinome: {self.codinome}"""
