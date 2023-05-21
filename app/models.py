from app import db
from datetime import datetime
from flask_login import UserMixin
import bcrypt
# Model containing User information. 
# Unique ids and usernames, and passwords stored as hashes.
# Hashes use bcrypt to provide more security than SHA256. 
# It also requries the salts to be saved
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    roomID = db.Column(db.Integer,db.ForeignKey("game_room.roomID"),index=True,default=-1)
    setting = db.relationship('Settings', backref='Settings', lazy='dynamic')
    salt = db.Column(db.String(128))
    password_hash = db.Column(db.String(128))

    def set_password(self,password):
        salt = bcrypt.gensalt()
        self.salt = salt
        self.password_hash = bcrypt.hashpw(password.encode("utf-8"), salt)

    def __repr__(self):
        return '<User {}, Room {}>'.format(self.username,self.roomID)
        # return '<User {}, email {}, password {}>'.format(self.username,self.email,self.password_hash)


# Stores user preferences about colour schemes

class Settings(db.Model):
    username = db.Column(
        db.String(64), db.ForeignKey("user.username"), primary_key=True,index=True
    )
    primaryColor = db.Column(db.String(7), default="#3a3341")
    secondaryColor = db.Column(db.String(7), default="#26282B")
    textColor = db.Column(db.String(7), default="#ffffff")

    def __repr__(self):
        return "<User {}, primaryColor {}, secondaryColor {}, textColor {}>".format(self.username, self.primaryColor, self.secondaryColor, self.textColor)

# Stores information about each individual room

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
    
# Stores information about the initial prompts for each room

class Prompts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomID = db.Column(db.Integer,db.ForeignKey("game_room.roomID"),index=True)
    role = db.Column(db.String(20))
    content = db.Column(db.String(400))
    def __repr__(self):
        return "<Room {}, Role {}, Content {}>".format(self.roomID, self.role, self.content)
    
# Stores previous message history for each user

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    roomID = db.Column(db.Integer,db.ForeignKey("game_room.roomID"),index=True)
    username = db.Column(db.String(30),db.ForeignKey("user.username"),index=True)
    text = db.Column(db.String(500))
    time = db.Column(db.DateTime)
    time = db.Column(db.DateTime)
    def __init__(self, *args, **kwargs):
        super(Message, self).__init__(*args, **kwargs)
        self.time = datetime.now()