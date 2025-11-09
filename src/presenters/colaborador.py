from exceptions.service import ServiceException
from filters.colaborador import ColaboradorFilter
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
                ("Listar", self.listar),
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

    def listar(self) -> None:
        colaboradores = None
        while colaboradores is None:
            print("Listar Colaboradores")
            print("Filtre pelo nome do colaborador (opcional)")
            nome = input(": ")
            if len(nome.strip()) == 0:
                nome = None

            try:
                colaboradores = self.colaborador_service.listar_colaboradores(
                    ColaboradorFilter(nome=nome)
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
