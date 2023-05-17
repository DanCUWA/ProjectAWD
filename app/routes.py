from app import app, db,socketio
from flask import render_template, request, escape, flash, redirect, session, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import *
from flask_socketio import emit
from app.forms import LoginForm, SignupForm
from app.controller import *
import bcrypt

@app.route("/")
@app.route("/index")
def index():
    return render_template("WelcomePage.html", title="MAIN")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return handleSignup()

@app.route("/login", methods=["GET", "POST"])
def login():
    return handleLogin()

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/settings", methods=['GET', 'POST'])
@login_required
def settings():
    return handleSettings()

@app.route("/rooms", methods=['GET', 'POST'])
@login_required
def rooms():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    rooms = GameRoom.query.all()
    return render_template('rooms.html', user=user, rooms=rooms)


@app.route("/rooms/deleteRoom", methods=['GET', 'POST'])
@login_required
def deleteRoom():
    return handleRoomDeletion()

@app.route("/createRoom", methods=['GET', 'POST'])
def createRoom():
    return handleRoomOnCreate()


@app.route("/createRoom/created", methods=['GET','POST'])
def createdRoom():
    return handleRoomCreated()

@app.route("/rooms/joinRoom", methods=['POST'])
@login_required
def joinRoom():
    return handleRoomJoin()

@app.route('/stats/<username>')
@login_required
def stats(username):
    return render_template('stats.html', username=escape(username))

@app.route('/profile')
@login_required
def profile(): 
    msgs = Message.query.filter_by(username=current_user.username).all()
    return render_template('profile.html',id=current_user.username,msgs=msgs)

@app.route('/chat/<cur_room>')
@login_required
def chat(cur_room):
    return handleChat(cur_room) 

@app.route("/get_username")
@login_required
def get_username():
    return {"username": current_user.username}