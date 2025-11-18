from flask import Blueprint, render_template, request, redirect, url_for
from exceptions.service import ServiceException


def create_blueprint(projeto_service, colaborador_service):
    bp = Blueprint("projetos", __name__, template_folder="templates")

    @bp.route("/")
    def listar():
        try:
            projetos = projeto_service.listar_projetos()
            return render_template("projetos/index.html", projetos=projetos)
        except ServiceException as e:
            return render_template("error.html", message=str(e))

    @bp.route("/criar", methods=["GET", "POST"])
    def criar():
        if request.method == "POST":
            nome = request.form.get("nome", "")
            codinome = request.form.get("codinome", "")
            descricao = request.form.get("descricao", "")
            try:
                projeto = projeto_service.criar_projeto(nome, codinome, descricao)
                return redirect(
                    url_for("projetos.consultar", codinome=projeto.codinome)
                )
            except ServiceException as e:
                return render_template("error.html", message=str(e))

        return render_template("projetos/criar.html")

    @bp.route("/consultar/<codinome>")
    def consultar(codinome):
        try:
            projeto = projeto_service.consultar_projeto(codinome)
            return render_template("projetos/consultar.html", projeto=projeto)
        except ServiceException as e:
            return render_template("error.html", message=str(e))

    @bp.route("/<codinome>/colaboradores")
    def listar_colaboradores(codinome):
        try:
            colaboradores = projeto_service.listar_colaboradores_do_projeto(codinome)
            return render_template(
                "projetos/listar_colaboradores.html",
                colaboradores=colaboradores,
                codinome=codinome,
            )
        except ServiceException as e:
            return render_template("error.html", message=str(e))

    @bp.route("/<codinome>/adicionar_colaborador", methods=["GET", "POST"])
    def adicionar_colaborador(codinome):
        if request.method == "POST":
            colaborador_codinome = request.form.get("colaborador_codinome", "")
            try:
                projeto_service.adicionar_colaborador_ao_projeto(
                    codinome, colaborador_codinome
                )
                return redirect(
                    url_for("projetos.listar_colaboradores", codinome=codinome)
                )
            except ServiceException as e:
                return render_template("error.html", message=str(e))
        return render_template("projetos/adicionar_colaborador.html", codinome=codinome)

    return bp
