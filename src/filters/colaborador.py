from dtos.projeto import ProjetoDTO


class ColaboradorFilter:
    def __init__(
        self, nome: str | None = None, projeto: ProjetoDTO | None = None
    ) -> None:
        self.nome = nome
        self.projeto = projeto
