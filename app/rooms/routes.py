from . import room_blueprint
# from app.controller import *
from .room_controller import *
@room_blueprint.route("/rooms", methods=['GET', 'POST'])
@login_required
def rooms():
    return handleRooms()

@room_blueprint.route("/rooms/deleteRoom", methods=['GET', 'POST'])
@login_required
def deleteRoom():
    return handleRoomDeletion()

@room_blueprint.route("/createRoom", methods=['GET', 'POST'])
@login_required
def createRoom():
    return handleRoomOnCreate()

@room_blueprint.route("/createRoom/created", methods=['GET','POST'])
@login_required
def createdRoom():
    return handleRoomCreated()

@room_blueprint.route("/rooms/joinRoom", methods=['POST'])
@login_required
def joinRoom():
    return handleRoomJoin()

@room_blueprint.route('/chat/<cur_room>')
@login_required
def chat(cur_room):
    return handleChat(cur_room) 
