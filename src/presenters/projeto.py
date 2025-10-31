from services.projeto import ProjetoService
from exceptions.service import ServiceException


class ProjetoPresenter:
    def __init__(self, projeto_service: ProjetoService) -> None:
        self.projeto_service = projeto_service

    def menu(self) -> None:
        opcoes = [
            ("Sair", None),
            ("Criar", self.criar),
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

            nome, funcao = opcoes[selecao]
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

        print(
            f'O projeto {projeto.codinome} "{projeto.nome}" foi criado com sucesso!\n'
        )
