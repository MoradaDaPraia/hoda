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
                ("Listar Colaboradores", self.listar_colaboradores),
                ("Adicionar Colaborador", self.adicionar_colaborador),
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

    def listar_colaboradores(self) -> None:
        colaboradores = None
        while colaboradores is None:
            print("Listar Colaboradores do Projeto")
            print("Insira o codinome do projeto")
            codinome = input(": ")

            try:
                colaboradores = self.projeto_service.listar_colaboradores_do_projeto(
                    codinome
                )
            except ServiceException as e:
                print(f"ERRO: {e}\n")
                continue

            if len(colaboradores) == 0:
                print("Nenhum colaborador foi encontrado.")
            else:
                for colaborador in colaboradores:
                    print(colaborador)

            print()

    def adicionar_colaborador(self) -> None:
        while True:
            print("Adicionar Colaborador ao Projeto")
            print("Insira o codinome do projeto")
            codinome = input(": ")
            print("Insira o codinome do colaborador")
            colaborador_codinome = input(": ")

            try:
                self.projeto_service.adicionar_colaborador_ao_projeto(
                    codinome, colaborador_codinome
                )
            except ServiceException as e:
                print(f"ERRO: {e}\n")
                continue

            print("O colaborador foi adicionado com sucesso!\n")
            break
