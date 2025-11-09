from dtos.colaborador import ColaboradorDTO
from dtos.projeto import ProjetoDTO
from exceptions.service import ServiceException
from filters.colaborador import ColaboradorFilter
from repositories.projetos import ProjetosRepository
from services.colaborador import ColaboradorService

NOME_DO_PROJETO_INVALIDO = "Nome do projeto inválido, deve ter entre 2-32 caracteres."
CODINOME_DO_PROJETO_INVALIDO = "Codinome do projeto inválido, deve ter entre 2-8 caracteres de apenas letras maiúsculas."
DESCRICAO_DO_PROJETO_INVALIDA = (
    "Descrição do projeto inválida, pode ter no máximo 255 caracteres."
)
JA_EXISTE_PROJETO_COM_ESTE_CODINOME = "Já existe um projeto com este codinome."
ESTE_PROJETO_NAO_EXISTE = "Este projeto não existe."


class ProjetoService:
    def __init__(
        self,
        projetos_repository: ProjetosRepository,
        colaborador_service: ColaboradorService,
    ) -> None:
        self.projetos_repository = projetos_repository
        self.colaborador_service = colaborador_service

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

        if (
            self.projetos_repository.consultar_projeto_por_codinome(codinome)
            is not None
        ):
            raise ServiceException(JA_EXISTE_PROJETO_COM_ESTE_CODINOME)

        projeto = self.projetos_repository.inserir_projeto(nome, codinome, descricao)

        return projeto

    def consultar_projeto(self, codinome: str) -> ProjetoDTO:
        if not self.__validar_codinome(codinome):
            raise ServiceException(CODINOME_DO_PROJETO_INVALIDO)

        projeto = self.projetos_repository.consultar_projeto_por_codinome(codinome)
        if projeto is None:
            raise ServiceException(ESTE_PROJETO_NAO_EXISTE)

        return projeto

    def listar_colaboradores_do_projeto(self, codinome: str) -> list[ColaboradorDTO]:
        projeto = self.consultar_projeto(codinome)
        return self.colaborador_service.listar_colaboradores(
            ColaboradorFilter(projeto_id=projeto.id)
        )

    def adicionar_colaborador_ao_projeto(
        self, codinome: str, colaborador_codinome: str
    ) -> None:
        projeto = self.consultar_projeto(codinome)
        colaborador = self.colaborador_service.consultar_colaborador(
            colaborador_codinome
        )

        self.projetos_repository.adicionar_colaborador_ao_projeto(projeto, colaborador)
