"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota
def index(): # função que gerencia rota
    """ Página inicial"""
    if '_user_id' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um  template


@bp.route("/dashboard") # cria uma rota
def dashboard(): # função que gerencia rota
    """ Painel de Vendas"""
    # if 'user' not in session:
    #     return redirect(url_for("auth.login"))
    # remova o login
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    vendas: list = [
        {"mês": "JANEIRO", "total": 139519.19},
        {"mês": "FEVEREIRO", "total": 123456.01},
        {"mês": "MARÇO", "total": 13.09},
        {"mês": "ABRIL", "total": 909090.01},
        {"mês": "MAIO", "total": 40028922.01},
        {"mês": "JUNHO", "total": 422419148.27},
        {"mês": "JULHO", "total": 10000000.01},
        {"mês": "AGOSTO", "total": 14567.00},
        {"mês": "SETEMBRO", "total": 354321.01},
        {"mês": "OUTUBRO", "total": 56678.01},
        {"mês": "NOVEMBRO", "total": 414679588.59},
        {"mês": "DEZEMBRO", "total": 25121999.01},

    ]# fim lista vendas

    
    return render_template("dashboard/index.html", title="Painel de Vendas", vendas=vendas, locale=locale) # Renderiza um template
    