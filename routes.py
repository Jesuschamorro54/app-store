import json
import functools
from flask import (render_template, redirect, blueprints,
                   session, request, url_for,)
from werkzeug.security import check_password_hash, generate_password_hash
from controllers import *

main = blueprints.Blueprint('main', __name__)

def param_loads(str_params: str):

    path = []
    for i in str_params.split("&"):
        path.append(i.split("="))

    dictionary = {}
    for key, val in path:
        dictionary.update({key : val})

    return dictionary

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

    # Llamas al controlador encargado de esa logica
    # response = main(event)

    print(request.view_args)
    params = param_loads(request.query_string.decode('utf-8'))

    print(params)
    return {'status': True, 'data': []}

    # return render_template('/home.html')

# ------------------- Methods Routes -------------------------

# POST:
@main.route('/clients', methods=['POST'])
def api_post_clients():
    
    event = {
        'body': {},
        'params': {},
        'user': {}
    }


@main.route('/distributors', methods=['POST'])
def api_post_distribuitors():
    event = {
        'body': {
            'name': "",
            'cellphone': "",
            'email': "",
            'company': ""
        },
        'params': {}
    }

    response = post_distributors.main(event)
    return response


@main.route('/distributors/<distributor_id>/articles', methods=['POST'])
def api_post_articles(distributor_id):

    body = json.loads(request.data)
    params = {}

    # View_args contiene los parametros de ruta de la peticion (request).
    for k, v in request.view_args.items(): 

        params.update({k:json.loads(v)})

    print(params)

    event = {
        'body': body,
        'params': params
    }

    print(event)

    response = post_articles.main(event)

    return response

def request_parse(request):
    
    body = {}
    params = {}

    # Params update
    for k, v in request.view_args.items():

        params.update({k : json.loads(v)})

    # Body create
    body = json.loads(request.data)

    # Response structure
    event = {
        'body': body,
        'params': params
    }

    return event


@main.route('/orders', methods=['POST'])
def api_post_orders():
    
    event = request_parse(request)
    response = post_orders.main(event)

    return response


@main.route('/details', methods=['POST'])
def api_post_details():
    pass


# GET
@main.route('/clients', methods=['GET'])
def api_get_clients():
    pass


@main.route('/clients', methods=['GET'])
def api_get_distributors():
    pass


@main.route('/articles', methods=['GET'])
def api_get_articles():
    event = {
        'body': {},
        'params': {
            'distributor_id': 0,
            'cost': 0
        },
        'user': {}
    }
    response = get_articles.main(event)

    return response


@main.route('/orders', methods=['GET'])
def api_get_orders():
    pass


@main.route('/details', methods=['GET'])
def api_get_details():
    pass


@main.route('/clients', methods=['PUT'])
def api_put_clients():
    pass


@main.route('/distributors', methods=['PUT'])
def api_put_distributors():
    pass


@main.route('/articles', methods=['PUT'])
def api_put_articles():
    pass


@main.route('/orders', methods=['PUT'])
def api_put_orders():
    pass


@main.route('/details', methods=['PUT'])
def api_put_details():
    pass


@main.route('/clients', methods=['DELETE'])
def api_delete_clients():
    pass


@main.route('/distributors', methods=['DELETE'])
def api_delete_distributors():
    pass


@main.route('/articles', methods=['DELETE'])
def api_delete_articles():
    pass


@main.route('/orders', methods=['DELETE'])
def api_delete_orders():
    pass


@main.route('/details', methods=['DELETE'])
def api_delete_details():
    pass