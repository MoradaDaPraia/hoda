from services.projeto import ProjetoService


class ProjetoPresenter:
    def __init__(self, projeto_service: ProjetoService) -> None:
        self.projeto_service = projeto_service
