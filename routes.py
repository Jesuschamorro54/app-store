import json
import functools
from flask import (render_template, redirect, blueprints,
                   session, request, url_for,)
from werkzeug.security import check_password_hash, generate_password_hash
from controllers import *

main = blueprints.Blueprint('main', __name__)

# ------------------------ Template Rendering ------------------------
@main.route('/', methods=['GET'])
def index():
    return redirect(url_for('main.home'))


@main.route('/home', methods=['GET'])
def home():

    return render_template('/home.html')


@main.context_processor
def general_variables():
    return {'appName': "Tiendita Tactica"}


# ------------------- Structure Methods -----------------

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

def param_loads(str_params: str):

    path = []
    for i in str_params.split("&"):
        path.append(i.split("="))

    dictionary = {}
    for key, val in path:
        dictionary.update({key : val})

    return dictionary

# ------------------- Methods Routes -------------------------

# POST:
@main.route('/clients', methods=['POST'])
def api_post_clients():
    
    event = request_parse(request)
    response = post_clients.main(event)

    return response


@main.route('/distributors', methods=['POST'])
def api_post_distribuitors():

    event = request_parse(request)
    response = post_distributors.main(event)

    return response


@main.route('/distributors/<distributor_id>/articles', methods=['POST'])
def api_post_articles(distributor_id):

    event = request_parse(request)
    response = post_articles.main(event)

    return response


@main.route('/clients/<client_id>/orders', methods=['POST'])
def api_post_orders(client_id):
    
    event = request_parse(request)
    response = post_orders.main(event)

    return response
 

# GET
@main.route('/clients/<client_id>', methods=['GET'])
def api_get_clients():

    event = request_parse(request)
    response = get_clients.main(event)

    return response


@main.route('/distributors/<distributor_id>', methods=['GET'])
def api_get_distributors():

    event = request_parse(request)
    response = get_distributors.main(event)

    return response


@main.route('/distributors/<distributor_id>/articles/<article_id>', methods=['GET'])
def api_get_articles(distributor_id):

    event = request_parse(request)
    response = get_articles.main(event)

    return response


@main.route('/clients/<client_id>/orders/<order_id>', methods=['GET'])
def api_get_orders(client_id):

    event = request_parse(request)
    response = get_orders.main(event)

    return response


# PUT:
@main.route('/clients/<client_id>', methods=['PUT'])
def api_put_clients():
    
    event = request_parse(request)
    response = put_clients.main(event)

    return response


@main.route('/distributors/<distributor_id>', methods=['PUT'])
def api_put_distributors():

    event = request_parse(request)
    response = put_distributors.main(event)

    return response



@main.route('/distributors/<distributor_id>/articles/<article_id>', methods=['PUT'])
def api_put_articles(distributor_id):

    event = request_parse(request)
    response = put_articles.main(event)

    return response



@main.route('/clients/<client_id>/orders/<order_id>', methods=['PUT'])
def api_put_orders(client_id):

    event = request_parse(request)
    response = put_orders.main(event)

    return response


# DELETE: 
@main.route('/clients/<client_id>', methods=['DELETE'])
def api_delete_clients():

    event = request_parse(request)
    response = delete_clients.main(event)

    return response


@main.route('/distributors/<distributor_id>', methods=['DELETE'])
def api_delete_distributors():

    event = request_parse(request)
    response = delete_distributors.main(event)

    return response


@main.route('/distributors/<distributor_id>/articles/<article_id>', methods=['DELETE'])
def api_delete_articles(distributor_id):

    event = request_parse(request)
    response = delete_articles.main(event)

    return response


@main.route('/clients/<client_id>/orders/<order_id>', methods=['DELETE'])
def api_delete_orders(client_id):

    event = request_parse(request)
    response = delete_orders.main(event)

    return response

