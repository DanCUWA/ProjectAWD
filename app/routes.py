from app import app
from flask import render_template
from flask import escape
@app.route('/')
@app.route('/index')
def index():
    return render_template('mainPage.html',title="MAIN")
@app.route('/signup', methods=['GET','POST'])
def signup():
    return render_template('signup.html')
@app.route('/stats/<username>')
def stats(username): 
    return render_template('stats.html',username=escape(username))
@app.route('/login')
def login(): 
    return render_template('login.html')
@app.route('/settings')
def settings(): 
    return render_template('settings.html')
@app.route('/rooms')
def rooms(): 
    return render_template('rooms.html')
@app.route('/profile/<user_id>')
def profile(user_id): 
    return render_template('profile.html',id=escape(user_id))

