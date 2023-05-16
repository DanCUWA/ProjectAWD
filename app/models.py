from app import db, login
from datetime import datetime
from flask_login import UserMixin

import bcrypt


@login.user_loader
def load_user(name):
    return User.query.get(name)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    # email = db.Column(db.String(120), index=True, unique=True)
    roomID = db.Column(db.Integer,db.ForeignKey("game_room.roomID"),index=True,default=-1)
    # rooms = db.relationship('GameRoom', backref='Game Rooms', lazy='dynamic')
    salt = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))

    # def __init__(self, **kwargs):
    #     super(User, self).__init__(**kwargs)

    def set_password(self,password):
        salt = bcrypt.gensalt()
        self.salt = salt
        self.password_hash = bcrypt.hashpw(password.encode("utf-8"), salt)

    def __repr__(self):
        return '<User {}, Room {}>'.format(self.username,self.roomID)
        # return '<User {}, email {}, password {}>'.format(self.username,self.email,self.password_hash)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))


class Stats(db.Model):
    username = db.Column(
        db.String(64), db.ForeignKey("user.username"), primary_key=True
    )

    def __repr__(self):
        return "<User {}>".format(self.username)


class Settings(db.Model):
    username = db.Column(
        db.String(64), db.ForeignKey("user.username"), primary_key=True,
    )
    primaryColor = db.Column(db.String(7), default="#000000")
    secondaryColor = db.Column(db.String(7), default="#FFFFFF")
    # seems unnecessary
    textColour = db.Column(db.String(64))

    def __repr__(self):
        return "<User {}, Colour {}>".format(self.username, self.textColour)


class GameRoom(db.Model):
    username = db.Column(
        db.String(64), db.ForeignKey("user.username"), index=True
    )
    roomID = db.Column(db.Integer, unique=True, primary_key = True)
    roomName = db.Column(db.String(30))
    playerNumber = db.Column(db.Integer)
    turnNumber = db.Column(db.Integer)
    scenario = db.Column(db.String)


    def __repr__(self):
        return "<User {}, Room access {}, roomName {}, playerNumber {}, turnNumber {}>".format(self.username, self.roomID, self.roomName, self.playerNumber, self.turnNumber)
    
class Prompts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomID = db.Column(db.Integer,db.ForeignKey("game_room.roomID"),index=True)
    role = db.Column(db.String(20))
    content = db.Column(db.String(400))
    def __repr__(self):
        return "<Room {}, Role {}, Content {}>".format(self.roomID, self.role, self.content)
    
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomID = db.Column(db.Integer,db.ForeignKey("game_room.roomID"),index=True)
    username = db.Column(db.String(30),db.ForeignKey("user.username"),index=True)
    text = db.Column(db.String(500))
    time = db.Column(db.DateTime)
    def __init__(self, *args, **kwargs):
        super(Message, self).__init__(*args, **kwargs)
        self.time = datetime.now()