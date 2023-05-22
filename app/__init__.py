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
login.login_view = 'main.login'

def create_app(): 
    app = Flask(__name__)
    app.config.from_object(Config)
    initialise(app)
    register_bps(app)
    return app

def initialise(app): 
    db.init_app(app)
    migrate.init_app(app,db)
    login.init_app(app)
    socketio.init_app(app)
    with app.app_context():
        db.create_all()

    from .models import User    
    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

def register_bps(app): 
    from app.rooms import room_blueprint
    from app.main import main_blueprint
    from app.users import user_blueprint

    app.register_blueprint(room_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint)
