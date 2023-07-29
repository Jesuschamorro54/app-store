import json
import functools
from flask import (render_template, redirect, blueprints,
                   session, request, url_for,)
from werkzeug.security import check_password_hash, generate_password_hash
from controllers import get_products

# from database.database import *


main = blueprints.Blueprint('main', __name__)


@main.context_processor
def general_variables():
    return {'appName': "Tiendita Tactica"}


# ------------------------ Template Rendering ------------------------
@main.route('/', methods=['GET'])
def index():
    return redirect(url_for('main.home'))


@main.route('/home', methods=['GET'])
def home():
    # Interpretar que quiere el front en este html
    # - Nuevos productos
    # - Productos destacados
    # - Datos de los productos
    event = {
        'params': {},
        'body': {},
        'user': {}
    }

    # Llamas al controlador encargado de esa logica
    response = get_products.main(event)

    # Imprimir la data que le enviarás al front
    print(f"Datos para el front: {None}")

    return render_template('/home.html')
