from dtos.projeto import ProjetoDTO
from exceptions.service import ServiceException
from repositories.projetos import ProjetosRepository

NOME_DO_PROJETO_INVALIDO = "Nome do projeto inválido, deve ter entre 2-32 caracteres."
CODINOME_DO_PROJETO_INVALIDO = "Codinome do projeto inválido, deve ter entre 2-8 caracteres de apenas letras maiúsculas."
DESCRICAO_DO_PROJETO_INVALIDA = (
    "Descrição do projeto inválida, pode ter no máximo 255 caracteres."
)
JA_EXISTE_PROJETO_COM_ESTE_CODINOME = "Já existe um projeto com este codinome."


class ProjetoService:
    def __init__(self, projeto_repository: ProjetosRepository) -> None:
        self.projeto_repository = projeto_repository

    def __validar_nome(self, nome: str) -> bool:
        return len(nome) >= 2 and len(nome) <= 32

    def __validar_codinome(self, codinome: str) -> bool:
        return (
            codinome.isalpha()
            and codinome.isupper()
            and len(codinome) >= 2
            and len(codinome) <= 8
        )

    def __validar_descricao(self, descricao: str) -> bool:
        return len(descricao) <= 255

    def criar_projeto(self, nome: str, codinome: str, descricao: str) -> ProjetoDTO:
        if not self.__validar_nome(nome):
            raise ServiceException(NOME_DO_PROJETO_INVALIDO)
        if not self.__validar_codinome(codinome):
            raise ServiceException(CODINOME_DO_PROJETO_INVALIDO)
        if not self.__validar_descricao(descricao):
            raise ServiceException(DESCRICAO_DO_PROJETO_INVALIDA)

        if self.projeto_repository.consultar_projeto_por_codinome(codinome) is not None:
            raise ServiceException(JA_EXISTE_PROJETO_COM_ESTE_CODINOME)

        projeto = self.projeto_repository.inserir_projeto(nome, codinome, descricao)

        return projeto
