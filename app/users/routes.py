from . import user_blueprint
# from app.controller import *
from .user_controller import *
@user_blueprint.route("/settings", methods=['GET', 'POST'])
@login_required
def settings():
    return handleSettings()

@user_blueprint.route('/profile')
@login_required
def profile(): 
    return handleProfile()

@user_blueprint.route("/logout")
@login_required
def logout():
    return handleLogout()

@user_blueprint.route("/get_username")
@login_required
def get_username():
    return getUsername()
