from presenters.projeto import ProjetoPresenter
from repositories.projetos import ProjetosRepository
from services.projeto import ProjetoService


if __name__ == "__main__":
    projeto_repository = ProjetosRepository()
    projeto_service = ProjetoService(projeto_repository)
    projeto_presenter = ProjetoPresenter(projeto_service)

    print(projeto_presenter)
