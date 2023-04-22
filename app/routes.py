from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return render_template('mainPage.html',title="MAIN")
@app.route('/signup')
def singup():
    return render_template('signup.html')