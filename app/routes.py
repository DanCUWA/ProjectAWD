from app import app
from flask import render_template, redirect, flash, jsonify
from flask import escape
from app import db
from app.forms import LoginForm, SignUpForm
from app.models import User
from flask_login import login_required, current_user, login_user, logout_user

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('mainPage.html',title="MAIN")

@app.route('/get_username')
def get_username():
    return {'username': current_user.username}

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(username=form.username.data) #, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(('/login'))
    return render_template('signup.html', title='SignUp', form=form)

@app.route('/stats/<username>')
def stats(username): 
    return render_template('stats.html',username=escape(username))

@app.route('/login', methods=['GET','POST'])
def login(): 
    if current_user.is_authenticated:
        return redirect('/index')
    form=LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(('/login'))
        login_user(user, remember=form.remember_me.data)
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(('/index'))

@app.route('/settings')
def settings(): 
    return render_template('settings.html')
@app.route('/rooms')
def rooms(): 
    return render_template('rooms.html')
@app.route('/profile/<user_id>')
def profile(user_id): 
    return render_template('profile.html',id=escape(user_id))

