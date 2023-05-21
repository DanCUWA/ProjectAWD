from flask_wtf import FlaskForm
import email_validator
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, ValidationError
from wtforms.validators import DataRequired, Email,EqualTo
from app.models import User

# Basic form for handling logins of existing users 

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In') 

# Basic form for handling sign ups for new users

class SignupForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')
    
    def validate_username(self,username): 
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already taken.')

