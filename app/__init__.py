from flask import Flask, Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO, send
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()
socketio = SocketIO()
migrate = Migrate()
login = LoginManager()
socketio = SocketIO()
login.login_view = 'login'

def create_app(): 
    app = Flask(__name__)
    app.config.from_object(Config)
    initialise(app)
    with app.app_context():
        from . import routes, controller, models

def initialise(app): 
    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)
    socketio.init_app(app)


# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# socketio = SocketIO(app)
# migrate = Migrate(app, db)
# login = LoginManager(app)
# login.login_view = 'login'
# from app import routes, models, controller
