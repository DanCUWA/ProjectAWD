from app import db
from flask import current_app,render_template, request, escape, flash, redirect, session, redirect, url_for
from flask_login import current_user, login_user, login_required
from app.models import *
from app.forms import * 
from . import main_blueprint
# Sets up initial database
@main_blueprint.before_request
def init_db():
    try: 
        db.create_all()
        db.session.commit()
        if User.query.filter_by(username="DCTEST").first() is None:
            u1 = User(username="DCTEST")
            u1.set_password("abc")
            db.session.add(u1)
            init_settings(u1)

        if User.query.filter_by(username="GAMEMASTER").first() is None:
            u2 = User(username="GAMEMASTER")
            u2.set_password("no_login")
            db.session.add(u2)
            init_settings(u2)

        if User.query.filter_by(username="Test").first() is None:
            u3 = User(username="Test")
            u3.set_password("abc")
            db.session.add(u3)
            init_settings(u3)
            
        db.session.commit()
    except: 
        print("Already initialised")
        pass
    print(User.query.all())

def init_settings(user):
    s = Settings(username=user.username)
    db.session.add(s)
    db.session.commit()

######################### ROUTE HANDLERS #########################

def handleSignup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        init_settings(user)
        flash("Congratulations, you are now a registered user!", "signup-success")
        return redirect(("/login"))
    return render_template("signup.html", title="SignUp", form=form)

def handleLogin():
    if current_user.is_authenticated:
        return redirect("/")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or user.password_hash != bcrypt.hashpw(
            form.password.data.encode("utf-8"), user.salt
        ):
            flash('Invalid username or password')
            return redirect("/login")
        else:
            login_user(user)
            next_page = request.args.get("next")
            if not next_page:
                next_page = "main.index"
            return redirect(next_page)
    return render_template("login.html", form=form)

def handleIntro():
    return render_template("IntroPage.html", title="Welcome")

def handleMain(): 
    return render_template("WelcomePage.html", title="MAIN")
