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
    # form = SignupForm()
    # if form.validate_on_submit():

    #     # add new user to the database
    #     user = User(username=form.username.data)  # , email=form.email.data)
    #     user.set_password(form.password.data)
    #     db.session.add(user)
    #     db.session.commit()
    #     init_all_db(user)
    #     flash("Congratulations, you are now a registered user!")
    #     return redirect(("/login"))
    # return render_template("signup.html", title="SignUp", form=form)


@app.route("/login", methods=["GET", "POST"])
def logins():
    return handleLogin()
    # if current_user.is_authenticated:
    #     return redirect("/")
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user is None or user.password_hash != bcrypt.hashpw(
    #         form.password.data.encode("utf-8"), user.salt
    #     ):
    #         flash('Invalid username or password')
    #         return redirect("/login")
    #     else:
    #         login_user(user)
    #         next_page = request.args.get("next")
    #         if not next_page:
    #             next_page = "index"
    #         return redirect(next_page)
    # return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/settings", methods=['GET', 'POST'])
@login_required
def settings():
    return handleSettings()
    # s = Settings.query.get(current_user.username)
    # if request.method == 'POST' and "username-submit" in request.form:
    #     user = User.query.filter_by(username=request.form['username']).first()
    #     if user is None:
    #         current_user.username = request.form['username']
    #         db.session.commit()
    #     else:
    #         flash('Username Already Taken')
    # if request.method == 'POST' and "color-submit" in request.form:
    #     s.primaryColor = request.form['primColour']
    #     s.secondaryColor = request.form['secoColour']
    #     s.textColor = request.form['textColour']
    #     db.session.commit()
    # if request.method == 'POST' and "default-submit" in request.form:
    #     s.primaryColor = '#3F3747'
    #     s.secondaryColor = '#26282B'
    #     s.textColor = '#ffffff'
    #     db.session.commit()
    # return render_template("settings.html", settings=s, user=current_user)

@login_required
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
    # user = User.query.filter_by(username=current_user.username).first_or_404()
    # if request.method == 'POST':
    #     deleteRoom = request.form['roomDelete']
    #     room_to_delete = GameRoom.query.get(deleteRoom)
    #     prompts_to_delete = Prompts.query.filter_by(roomID=room_to_delete.roomID).all()
    #     messages_to_delete = Message.query.filter_by(roomID=room_to_delete.roomID).all()
    #     db.session.delete(room_to_delete)
    #     for prompts in prompts_to_delete:
    #         db.session.delete(prompts)
    #     for messages in messages_to_delete:
    #         db.session.delete(messages)
    #     db.session.commit()

    # rooms = GameRoom.query.filter_by(username=current_user.username).all()
    # return render_template('rooms.html', user=user, rooms=rooms)

@app.route("/createRoom", methods=['GET', 'POST'])
def createRoom():
    if request.method == 'POST':
        session['room_name'] = request.form['room_name']
        session['num_players'] = int(request.form['num_players'])
        
    return render_template('CreateRoom.html')

@app.route("/createRoom/created", methods=['GET','POST'])
def createdRoom():
    return handleRoomCreation()
    # user = User.query.filter_by(username=current_user.username).first_or_404()
    # if request.method == 'POST':
    #     room_name = session['room_name']
    #     num_players = session['num_players']
    #     startScenario = request.form['scenario']
    #     # Create a new Room object and set the necessary attributes
    #     room = GameRoom(username=user.username, roomName=room_name, playerNumber=num_players, turnNumber=0, scenario = startScenario)
    #     startingPrompt = starting_prompt()
    #     prompt = Prompts(roomID=room.roomID, role="system", content=startingPrompt)


    #     # Add the room to the database
    #     db.session.add(room)
    #     db.session.add(prompt)
    #     db.session.commit()
    # rooms = GameRoom.query.all()
    # return render_template('rooms.html', user=user, rooms=rooms)


@login_required
@app.route("/rooms/joinRoom", methods=['POST'])
def joinRoom():
    return handleRoomJoin()
    # roomNum = request.form['roomJoin']
    # user = User.query.filter_by(username=current_user.username).first_or_404()
    # n_users = len(User.query.filter_by(roomID=roomNum).all())
    # room = GameRoom.query.get(roomNum)
    # print("TRYING TO JOIN ROOM " + str(room.playerNumber))
    # if room.playerNumber > n_users: 
    #     session['room'] = roomNum
    #     return redirect('/chat/' + roomNum)
    # else: 
    #     flash("Room full!")
    #     return redirect(url_for('rooms'))

@login_required
@app.route('/stats/<username>')
def stats(username):
    return render_template('stats.html', username=escape(username))

@login_required
@app.route('/profile')
def profile(): 
    msgs = Message.query.filter_by(username=current_user.username).all()
    return render_template('profile.html',id=current_user.username,msgs=msgs)

@login_required
@app.route('/chat/<cur_room>')
def chat(cur_room):
    return handleChat(cur_room) 
    # user = User.query.filter_by(username=current_user.username).first_or_404()
    # if (cur_room == session['room']):
    #     s = Settings.query.get(user.username)
    #     return render_template("chat.html", title="MAIN", name=user.username, room=cur_room, setting = s)
    # else: 
    #     return redirect(url_for('rooms'))

@login_required
@app.route("/get_username")
def get_username():
    return {"username": current_user.username}