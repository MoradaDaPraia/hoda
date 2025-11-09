from dtos.colaborador import ColaboradorDTO
from exceptions.service import ServiceException
from repositories.colaboradores import ColaboradoresRepository
import hashlib

NOME_DO_COLABORADOR_INVALIDO = (
    "Nome do colaborador inválido, deve ter entre 8-64 caracteres."
)
CODINOME_DO_COLABORADOR_INVALIDO = "Codinome do colaborador inválido, deve ter entre 4-16 caracteres sem espaços, acentos ou caracteres especiais."
SENHA_DO_COLABORADOR_INVALIDA = (
    "Senha do colaborador inválida, deve ter no máximo 64 caracteres."
)
JA_EXISTE_COLABORADOR_COM_ESTE_CODINOME = (
    "Já existe um colaborador cadastrado com este codinome."
)


class ColaboradorService:
    def __init__(self, colaboradores_repository: ColaboradoresRepository) -> None:
        self.colaboradores_repository = colaboradores_repository

    def __validar_nome(self, nome: str) -> bool:
        return len(nome) >= 8 and len(nome) <= 64

    def __validar_codinome(self, codinome: str) -> bool:
        return (
            len(codinome) >= 4
            and len(codinome) <= 16
            and codinome.isascii()
            and codinome.isprintable()
            and not codinome.isspace()
        )

    def __validar_senha(self, senha: str) -> bool:
        return len(senha) <= 64

    def criar_colaborador(self, nome: str, codinome: str, senha: str) -> ColaboradorDTO:
        if not self.__validar_nome(nome):
            raise ServiceException(NOME_DO_COLABORADOR_INVALIDO)
        if not self.__validar_codinome(codinome):
            raise ServiceException(CODINOME_DO_COLABORADOR_INVALIDO)
        if not self.__validar_senha(senha):
            raise ServiceException(SENHA_DO_COLABORADOR_INVALIDA)

        if (
            self.colaboradores_repository.consultar_colaborador_por_codinome(codinome)
            is not None
        ):
            raise ServiceException(JA_EXISTE_COLABORADOR_COM_ESTE_CODINOME)

        senha_hash = hashlib.md5(senha.encode()).hexdigest()
        colaborador = self.colaboradores_repository.inserir_colaborador(
            nome, codinome, senha_hash
        )

        return colaborador
