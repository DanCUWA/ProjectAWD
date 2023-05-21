from flask import Blueprint


room_blueprint = Blueprint('rooms', __name__)

from . import routes