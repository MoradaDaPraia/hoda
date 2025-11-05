class ProjetoDTO:
    def __init__(self, id: int, nome: str, codinome: str, descricao: str) -> None:
        self.id = id
        self.nome = nome
        self.codinome = codinome
        self.descricao = descricao

    def __str__(self) -> str:
        return f"""Projeto
    Nome: {self.nome}
    Codinome: {self.codinome}
    Descricao: {self.descricao}"""
