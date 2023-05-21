from flask import Blueprint


user_blueprint = Blueprint('users', __name__)

from . import routes
