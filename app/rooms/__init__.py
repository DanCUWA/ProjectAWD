from flask import Blueprint


room_blueprint = Blueprint('rooms', __name__, template_folder='templates')

from . import routes