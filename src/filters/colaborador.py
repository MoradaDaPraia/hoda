from dtos.projeto import ProjetoDTO


class ColaboradorFilter:
    def __init__(self, nome: str | None = None, projeto_id: int | None = None) -> None:
        self.nome = nome
        self.projeto_id = projeto_id
