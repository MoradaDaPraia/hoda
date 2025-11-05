from services.projeto import ProjetoService, ESTE_PROJETO_NAO_EXISTE
from exceptions.service import ServiceException


class ProjetoPresenter:
    def __init__(self, projeto_service: ProjetoService) -> None:
        self.projeto_service = projeto_service

    def menu(self) -> None:
        opcoes = [
            ("Sair", None),
            ("Criar", self.criar),
            ("Consultar", self.consultar),
        ]
        selecao = 999
        while selecao != 0:
            print("""Projetos""")
            for i, (nome, _) in enumerate(opcoes):
                print(f"- {nome} ({i})")

            try:
                selecao = int(input("Selecione uma opção: "))
                if selecao < 0 or selecao >= len(opcoes):
                    raise Exception()
            except Exception:
                print("Seleção inválida!\n")
                continue

            if selecao == 0:
                break

            _, funcao = opcoes[selecao]
            print()
            funcao()

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
