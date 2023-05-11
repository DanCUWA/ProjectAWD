from app import app, db,socketio
from flask import render_template, request, escape, flash, redirect, session, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from flask_socketio import emit
from app.models import User, Settings, Stats
from app.forms import LoginForm, SignupForm
import bcrypt
import openai 
import os

openai.api_key = os.environ['GPT_KEY']

def init_all_db(user):
    s = Settings(username=user)
    st = Stats(username=user)
    db.session.add(s)
    db.session.add(st)
    db.session.commit()

def gpt_response(text):
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=text,
    max_tokens=50
    )
    return response.choices[0].text



@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('player-mes')
def handle_playerqs(data): 
    print(data)
    print("Got player message" + data['data'])
    name = "Anon"
    if current_user.is_authenticated: 
        name = current_user.username
    socketio.emit('server-response',{'message':data['data'],'name':name})

@socketio.on('next-turn')
def handle_turn(data): 
    room = data['roomID']
    print("HANDLING")
    # req = gpt_response("Give me a short scenario for a DnD like RPG")
    req = "Sorry am unhooked :("
    print("req " + req)
    socketio.emit('gpt-res',{'message':req})



@socketio.on('connect')
def connect_handler():
    print("Server side connections")
    # if current_user.is_authenticated:
    #     emit('my response',
    #          {'message': '{0} has joined'.format(current_user.name)},
    #          broadcast=True)
    # else:
    #     return False  # not allowed here\
    
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


@app.route("/rooms")
def rooms():
    return render_template("rooms.html")


@login_required
@app.route("/stats/")
def stats():
    return render_template("stats.html")
