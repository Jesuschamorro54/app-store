import json
import functools
from flask import ( render_template, redirect, blueprints, session, request, url_for,)
from werkzeug.security import check_password_hash, generate_password_hash

from database.database import *


main = blueprints.Blueprint('main', __name__)

@main.context_processor
def general_variables():
    return { 'appName': "Tiendita Tactica" }


# ------------------------ Template Rendering ------------------------
@main.route('/', methods=['GET'])
def index():
    return redirect(url_for('main.home'))

@main.route('/home', methods=['GET'])
def home():
    return render_template('/index.html')




