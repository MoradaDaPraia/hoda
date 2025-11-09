from presenters.presenter import Presenter
from services.projeto import ProjetoService, ESTE_PROJETO_NAO_EXISTE
from exceptions.service import ServiceException


class ProjetoPresenter(Presenter):
    def __init__(self, projeto_service: ProjetoService) -> None:
        super().__init__()
        self.projeto_service = projeto_service

    def menu(self) -> None:
        self.desenhar_menu(
            "Projetos",
            [
                ("Sair", None),
                ("Criar", self.criar),
                ("Consultar", self.consultar),
            ],
        )

    def criar(self) -> None:
        projeto = None
        while projeto is None:
            print("Criar Projeto")
            print("Insira o nome do projeto (ex. Colégio Falcão)")
            nome = input(": ")
            print("Insira o codinome do projeto (ex. FLC)")
            codinome = input(": ")
            print("Insira a descriçã̀o do projeto (opcional)")
            descricao = input(": ")

            try:
                projeto = self.projeto_service.criar_projeto(nome, codinome, descricao)
            except ServiceException as e:
                print(f"ERRO: {e}\n")

        print(f"{projeto}\nO projeto foi criado com sucesso!\n")

    def consultar(self) -> None:
        projeto = None
        while projeto is None:
            print("Consultar Projeto")
            print("Insira o codinome do projeto")
            codinome = input(": ")
            try:
                projeto = self.projeto_service.consultar_projeto(codinome)
            except ServiceException as e:
                print(f"ERRO: {e}\n")
                if str(e) == ESTE_PROJETO_NAO_EXISTE:
                    return
                continue

        print(f"{projeto}\n")
