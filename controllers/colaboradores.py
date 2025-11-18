from flask import Blueprint, render_template, request, redirect, url_for
from exceptions.service import ServiceException
from filters.colaborador import ColaboradorFilter


def create_blueprint(colaborador_service):
    bp = Blueprint("colaboradores", __name__, template_folder="templates")

    @bp.route("/criar", methods=["GET", "POST"])
    def criar():
        if request.method == "POST":
            nome = request.form.get("nome", "")
            codinome = request.form.get("codinome", "")
            senha = request.form.get("senha", "")

            try:
                colaborador_service.criar_colaborador(nome, codinome, senha)
                return redirect(url_for("colaboradores.listar"))
            except ServiceException as e:
                return render_template("error.html", message=str(e))

        return render_template("colaboradores/criar.html")

    @bp.route("/")
    def listar():
        nome = request.args.get("nome")
        if nome is not None and len(nome.strip()) == 0:
            nome = None
        try:
            colaboradores = colaborador_service.listar_colaboradores(
                ColaboradorFilter(nome=nome)
            )

            return render_template(
                "colaboradores/index.html", colaboradores=colaboradores
            )
        except ServiceException as e:
            return render_template("error.html", message=str(e))

    return bp
