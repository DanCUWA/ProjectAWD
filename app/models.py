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
    salt = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def set_password(self,password):
        salt = bcrypt.gensalt()
        self.salt = salt
        self.password_hash = bcrypt.hashpw(password.encode("utf-8"), salt)

    def __repr__(self):
        return '<User {}>'.format(self.username)
        # return '<User {}, email {}, password {}>'.format(self.username,self.email,self.password_hash)

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))


class Stats(db.Model):
    username = db.Column(
        db.String(64), db.ForeignKey("user.username"), primary_key=True, index=True
    )

    def __repr__(self):
        return "<User {}>".format(self.username)


class Settings(db.Model):
    username = db.Column(
        db.String(64), db.ForeignKey("user.username"), primary_key=True, index=True
    )
    primaryColor = db.Column(db.String(7), default="#000000")
    secondaryColor = db.Column(db.String(7), default="#FFFFFF")
    # seems unnecessary
    textColour = db.Column(db.String(64))

    def __repr__(self):
        return "<User {}, Colour {}>".format(self.username, self.textColour)


class GameRoom(db.Model):
    username = db.Column(
        db.String(64), db.ForeignKey("user.username"), primary_key=True, index=True
    )
    roomID = db.Column(db.Integer, unique=True, index=True)
    roomName = db.Column(db.String(30), index=True)
    playerNumber = db.Column(db.Integer, index=True)
    turnNumber = db.Column(db.Integer, index=True)


    def __repr__(self):
        return "<User {}, Room access {}, roomName {}, playerNumber {}, turnNumber {}>".format(self.username, self.roomID, self.roomName, self.playerNumber, self.turnNumber)
