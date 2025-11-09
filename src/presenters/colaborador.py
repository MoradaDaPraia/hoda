from exceptions.service import ServiceException
from presenters.presenter import Presenter
from services.colaborador import ColaboradorService


class ColaboradorPresenter(Presenter):
    def __init__(self, colaborador_service: ColaboradorService):
        super().__init__()
        self.colaborador_service = colaborador_service

    def menu(self) -> None:
        self.desenhar_menu(
            "Colaboradores",
            [
                ("Sair", None),
                ("Criar", self.criar),
            ],
        )

    def criar(self) -> None:
        colaborador = None
        while colaborador is None:
            print("Criar Colaborador")
            print("Insira o nome do colaborador (ex. Serafim Pouza)")
            nome = input(": ")
            print("Insira o codinome do colaborador (ex. serafim.pouza)")
            codinome = input(": ")
            print("Crie uma senha para o colaborador (opcional)")
            senha = input(": ")

            try:
                colaborador = self.colaborador_service.criar_colaborador(
                    nome, codinome, senha
                )
            except ServiceException as e:
                print(f"ERRO: {e}\n")

            print(f"{colaborador}\nO colaborador foi criado com sucesso!\n")
