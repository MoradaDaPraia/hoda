from presenters.colaborador import ColaboradorPresenter
from presenters.principal import PrincipalPresenter
from presenters.projeto import ProjetoPresenter
from repositories.colaboradores import ColaboradoresRepository
from repositories.projetos import ProjetosRepository
from services.colaborador import ColaboradorService
from services.projeto import ProjetoService


if __name__ == "__main__":
    projetos_repository = ProjetosRepository()
    colaboradores_repository = ColaboradoresRepository()

    colaborador_service = ColaboradorService(colaboradores_repository)
    projeto_service = ProjetoService(projetos_repository, colaborador_service)

    projeto_presenter = ProjetoPresenter(projeto_service)
    colaborador_presenter = ColaboradorPresenter(colaborador_service)

    principal_presenter = PrincipalPresenter(projeto_presenter, colaborador_presenter)

    principal_presenter.menu()
