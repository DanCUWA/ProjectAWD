from app import db
from flask import render_template, request, escape, flash, redirect, session, redirect, url_for
from flask_login import current_user, logout_user, login_required
from app.models import *
from app.forms import * 

def handleProfile():
    msgs = Message.query.filter_by(username=current_user.username)
    all_msgs = msgs.all()
    msg_rms = msgs.group_by(Message.roomID).all()
    room_ids = map(lambda m:m.roomID,msg_rms)
    rooms = []
    for r in room_ids: 
        room = GameRoom.query.get(r)
        rooms.append(room)
    print(all_msgs)
    return render_template('profile.html',id=current_user.username,msgs=all_msgs,rooms=rooms)

def handleLogout(): 
    logout_user()
    return redirect("/")

def getUsername():
    return {"username": current_user.username}

def handleSettings(): 
    s = Settings.query.get(current_user.username)
    if request.method == 'POST' and "username-submit" in request.form:
        user = User.query.filter_by(username=request.form['username']).first()
        if user is None:
            messages = Message.query.filter_by(username=current_user.username).all()
            new_username = request.form['username']
            current_user.username = new_username
            s.username = new_username
            for m in messages:
                m.username = new_username
            db.session.commit()
        else:
            flash('Username Already Taken', 'username-error')
    if request.method == 'POST' and "color-submit" in request.form:
        s.primaryColor = request.form['primColour']
        s.secondaryColor = request.form['secoColour']
        s.textColor = request.form['textColour']
        db.session.commit()
    if request.method == 'POST' and "default-submit" in request.form:
        s.primaryColor = '#3a3341'
        s.secondaryColor = '#26282B'
        s.textColor = '#ffffff'
        db.session.commit()
    if request.method == 'POST' and "password-submit" in request.form:
        user = User.query.filter_by(username=current_user.username).first()
        password1 = request.form['password1']
        password2 = request.form['password2']
        if password1 == password2:
            user.set_password(password1)
            db.session.commit()
        else:
            flash('Passwords do NOT match','password-error')
    if request.method == 'POST' and "delete-submit" in request.form:
        if(current_user.username == request.form["username"]):
            user = User.query.filter_by(username=current_user.username).first_or_404()
            messages_to_delete = Message.query.filter_by(username=current_user.username).all()
            logout_user()
            db.session.delete(s)
            for m in messages_to_delete:
                db.session.delete(m)
            db.session.delete(user)
            db.session.commit()
            return redirect("/")
    return render_template("settings.html", settings=s, user=current_user)
