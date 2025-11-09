from presenters.projeto import ProjetoPresenter
from presenters.colaborador import ColaboradorPresenter
from presenters.presenter import Presenter


class PrincipalPresenter(Presenter):
    def __init__(
        self,
        projeto_presenter: ProjetoPresenter,
        colaborador_presenter: ColaboradorPresenter,
    ) -> None:
        super().__init__()
        self.projeto_presenter = projeto_presenter
        self.colaborador_presenter = colaborador_presenter

    def menu(self) -> None:
        self.desenhar_menu(
            "Hoda - Menu Principal",
            [
                ("Sair", None),
                ("Projetos", self.projeto_presenter.menu),
                ("Colaboradores", self.colaborador_presenter.menu),
            ],
        )
