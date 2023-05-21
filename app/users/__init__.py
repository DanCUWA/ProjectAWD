from flask import Blueprint


user_blueprint = Blueprint('users', __name__, template_folder='templates')

from . import routes
