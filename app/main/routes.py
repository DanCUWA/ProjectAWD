from . import main_blueprint
# from app.controller import *
from .main_controller import *
@main_blueprint.route("/")
@main_blueprint.route("/intro")
def intro():
    return handleIntro()

@main_blueprint.route("/index")
def index():
    return handleMain()

@main_blueprint.route("/signup", methods=["GET", "POST"])
def signup():
    return handleSignup()

@main_blueprint.route("/login", methods=["GET", "POST"])
def login():
    return handleLogin()
