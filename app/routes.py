# from app import app
from flask import current_app, Blueprint
from flask_login import login_required
from app.controller import *

# Contains all routes, along with necessary logins. 
# All logic handled in controller.

# Public routes

@current_app.route("/")
@current_app.route("/intro")
def intro():
    return handleIntro()

@current_app.route("/index")
def index():
    return handleMain()

@current_app.route("/signup", methods=["GET", "POST"])
def signup():
    return handleSignup()

@current_app.route("/login", methods=["GET", "POST"])
def login():
    return handleLogin()

# User information routes 

@current_app.route("/settings", methods=['GET', 'POST'])
@login_required
def settings():
    return handleSettings()

@current_app.route('/profile')
@login_required
def profile(): 
    return handleProfile()

@current_app.route("/logout")
def logout():
    return handleLogout()

@current_app.route("/get_username")
@login_required
def get_username():
    return getUsername()

# Game room handling 

@current_app.route("/rooms", methods=['GET', 'POST'])
@login_required
def rooms():
    return handleRooms()

@current_app.route("/rooms/deleteRoom", methods=['GET', 'POST'])
@login_required
def deleteRoom():
    return handleRoomDeletion()

@current_app.route("/createRoom", methods=['GET', 'POST'])
@login_required
def createRoom():
    return handleRoomOnCreate()

@current_app.route("/createRoom/created", methods=['GET','POST'])
@login_required
def createdRoom():
    return handleRoomCreated()

@current_app.route("/rooms/joinRoom", methods=['POST'])
@login_required
def joinRoom():
    return handleRoomJoin()

@current_app.route('/chat/<cur_room>')
@login_required
def chat(cur_room):
    return handleChat(cur_room) 


