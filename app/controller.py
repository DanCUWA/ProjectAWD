from app import app,db,socketio
from flask import render_template, request, escape, flash, redirect, session, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.models import *
from app.forms import * 
from flask_socketio import emit
import openai, os
@app.before_first_request
def make_base(): 
    db.drop_all()
    db.create_all()
    db.session.commit()
    u1 = User(username="DCTEST")
    u1.set_password("abc")
    u2 = User(username="GAMEMASTER")
    u2.set_password("no_login")
    u3 = User(username="Test")
    u3.set_password("abc")
    room = GameRoom(username=u1.username, roomName="lolhi", playerNumber=4, turnNumber=0)
    db.session.add_all([u1,u2,u3,room])
    db.session.commit()
    print(User.query.all())

# openai.api_key = os.environ['GPT_KEY']
def gpt_response(text):
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=text,
    max_tokens=50
    )
    return response.choices[0].text
def add_message(msg): 
    if current_user.is_authenticated:
        #CHANGE ROOM ID
        m = Message(username=current_user.username,text=msg,roomID=1)
        db.session.add(m)
        db.session.commit()

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
    add_message(data['data'])
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