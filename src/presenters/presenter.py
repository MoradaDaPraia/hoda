from abc import ABC
from typing import Callable


class Presenter(ABC):
    def desenhar_menu(self, titulo: str, opcoes: list[tuple[str, Callable | None]]):
        selecao = 999
        while selecao != 0:
            print(titulo)
            for i, (nome, _) in enumerate(opcoes):
                print(f"- {nome} ({i})")

            try:
                selecao = int(input("Selecione uma opção: "))
                if selecao < 0 or selecao >= len(opcoes):
                    raise Exception()
            except Exception:
                print("Seleção inválida!\n")
                continue

            _, funcao = opcoes[selecao]
            print()

            if funcao is None:
                break
            funcao()
