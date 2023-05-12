from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

@socketio.on('joined', namespace='/mainPage')
def joined(message):
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has come to the party.'}, room = room)

@socketio.on('text', namespace='/mainPage')
def text(message):
    room = session.get('room')
    emit('message', {'msg':session.get('name') + ':' + message['msg']}, room = room)

@socketio.on('left', namespace='/mainPage')
def left(message):
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

