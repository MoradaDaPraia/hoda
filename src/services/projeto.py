from repositories.projetos import ProjetosRepository


class ProjetoService:
    def __init__(self, projeto_repository: ProjetosRepository) -> None:
        self.projeto_repository = projeto_repository
