# Hoda: Um Organizador de Tarefas por Projeto

## Integrates

Andrey Arthur Sousa e Silva (andrey.arthur@unisantos.br)
Rafael Menezes de Oliveira (rafael.menezes@unisantos.br)
Victor Hugo Galeno de Sousa (victorhsousa@unisantos.br)

## Descrição

O Hoda é um sistema de gerenciamento de tarefas por projeto, desenvolvido para organizar atividades dentro de projetos. Foram implementadas em entidades: Projeto, que contém identificador, codinome, nome, descrição, além da lista de colaboradores envolvidos; e Colaborador, que possui identificador, nome, codinome e senha opcional. Nesta implementação, o Hoda permite a criação e listagem de projetos, a inclusão de colaboradores e a associação desses colaboradores aos projetos. Dessa forma, o sistema objetiva otimizar a gestão de projetos, permitindo o controle do andamento de projetos por uma via digital.

## Rodando o Projeto

Em Linux:

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python webapp.py
```

Em Windows (no cmd):

```sh
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python webapp.py
```
