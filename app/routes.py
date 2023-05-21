from app import app
from flask_login import login_required
from app.controller import *

# Contains all routes, along with necessary logins. 
# All logic handled in controller.

# Public routes

@app.route("/")
@app.route("/intro")
def intro():
    return handleIntro()

@app.route("/index")
def index():
    return handleMain()

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return handleSignup()

@app.route("/login", methods=["GET", "POST"])
def login():
    return handleLogin()

# User information routes 

@app.route("/settings", methods=['GET', 'POST'])
@login_required
def settings():
    return handleSettings()

@app.route('/profile')
@login_required
def profile(): 
    return handleProfile()

@app.route("/logout")
def logout():
    return handleLogout()

@app.route("/get_username")
@login_required
def get_username():
    return getUsername()

# Game room handling 

@app.route("/rooms", methods=['GET', 'POST'])
@login_required
def rooms():
    return handleRooms()

@app.route("/rooms/deleteRoom", methods=['GET', 'POST'])
@login_required
def deleteRoom():
    return handleRoomDeletion()

@app.route("/createRoom", methods=['GET', 'POST'])
@login_required
def createRoom():
    return handleRoomOnCreate()

@app.route("/createRoom/created", methods=['GET','POST'])
@login_required
def createdRoom():
    return handleRoomCreated()

@app.route("/rooms/joinRoom", methods=['POST'])
@login_required
def joinRoom():
    return handleRoomJoin()

@app.route('/chat/<cur_room>')
@login_required
def chat(cur_room):
    return handleChat(cur_room) 


