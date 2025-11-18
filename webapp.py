# webapp.py
import sys
from flask import Flask, render_template

# adiciona seu src ao path para importar seus serviços/repositories
sys.path.append("./src")

from repositories.projetos import ProjetosRepository
from repositories.colaboradores import ColaboradoresRepository
from services.projeto import ProjetoService
from services.colaborador import ColaboradorService
from exceptions.service import ServiceException

from controllers import projetos as projetos_controller
from controllers import colaboradores as colaboradores_controller


def create_app() -> Flask:
    app = Flask(__name__)

    projetos_repo = ProjetosRepository()
    colaboradores_repo = ColaboradoresRepository()

    colaborador_service = ColaboradorService(colaboradores_repo)
    projeto_service = ProjetoService(projetos_repo, colaborador_service)

    app.register_blueprint(
        projetos_controller.create_blueprint(projeto_service, colaborador_service),
        url_prefix="/projetos",
    )
    app.register_blueprint(
        colaboradores_controller.create_blueprint(colaborador_service),
        url_prefix="/colaboradores",
    )

    @app.route("/")
    def index():
        return render_template("base.html")

    @app.errorhandler(ServiceException)
    def handle_service_exception(e):
        return render_template("error.html", message=str(e)), 400

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        return render_template("error.html", message=str(e)), 500

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
