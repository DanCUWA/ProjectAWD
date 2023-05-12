from app import app, db,socketio
from flask import render_template, request, escape, flash, redirect, session, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import *
from flask_socketio import emit
from app.forms import LoginForm, SignupForm
import bcrypt
import openai 
import os

# openai.api_key = os.environ['GPT_KEY']
    
@app.route("/")
@app.route("/index")
def index():
    """Chat room. The user's name and room must be stored in
    the session."""
    # name = session.get('name', 'LostBoi0')
    room = session.get('room', '1')
    if current_user.is_authenticated: 
        name = current_user.username
    else: 
        name = "Not logged in"
    # if name == '' or room == '':
    #     return redirect(url_for('index'))
    return render_template("mainPage.html", title="MAIN", name=name, room=room)


@app.route("/get_username")
def get_username():
    return {"username": current_user.username}


@app.route("/signup", methods=["GET", "POST"])
def signup():

    form = SignupForm()
    if form.validate_on_submit():

        # add new user to the database
        user = User(username=form.username.data)  # , email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(("/login"))
    return render_template("signup.html", title="SignUp", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user.password_hash != bcrypt.hashpw(
            form.password.data.encode("utf-8"), user.salt
        ):
            flash("Incorrect password")
            return redirect("/")
        if user is None:
            flash("User does not exist")
            return redirect("/")
        login_user(user)
        next_page = request.args.get("next")
        if not next_page:
            next_page = "index"
        return redirect(next_page)
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/settings")
@login_required
def settings():
    s = Settings.query.get(current_user.username)
    return render_template("settings.html", settings=s)


@app.route("/rooms", methods=['GET', 'POST'])
def rooms():
    user = User.query.filter_by(username=current_user.username).first_or_404()

    if request.method == 'POST':
        room_name = request.form['room_name']
        num_players = int(request.form['num_players'])

        # Create a new Room object and set the necessary attributes
        room = GameRoom(username=user.username, roomName=room_name, playerNumber=num_players, turnNumber=0)

        # Add the room to the database
        db.session.add(room)
        db.session.commit()

    rooms = GameRoom.query.filter_by(username=current_user.username).all()


    return render_template('rooms.html', user=user, rooms=rooms)

@app.route("/rooms/deleteRoom", methods=['GET', 'POST'])
def deleteRoom():
    user = User.query.filter_by(username=current_user.username).first_or_404()
    if request.method == 'POST':
            deleteRoom = request.form['roomDelete']
            room_to_delete = GameRoom.query.get(deleteRoom)
            db.session.delete(room_to_delete)
            db.session.commit()

    rooms = GameRoom.query.filter_by(username=current_user.username).all()
    return render_template('rooms.html', user=user, rooms=rooms)

@login_required
@app.route('/stats/<username>')
def stats(username): 
    return render_template('stats.html',username=escape(username))

@login_required
@app.route('/profile')
def profile(): 
    msgs = Message.query.filter_by(username=current_user.username).all()
    return render_template('profile.html',id=current_user.username,msgs=msgs)

