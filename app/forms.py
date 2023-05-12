from flask_wtf import FlaskForm
import email_validator
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, ValidationError
from wtforms.validators import DataRequired, Email,EqualTo
from app.models import User
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In') 

class SignupForm(FlaskForm): 
    username = StringField('Username', validators=[DataRequired()])
    # email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')
    
    def validate_username(self,username): 
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already taken.')

    # def validate_error(self,email): 
    #     if User.query.filter_by(email=email).first() is not None:
    #         raise ValidationError("Email is already in use.")

    # def validate_password(form,field): 
    #     print("field " + field.data + " pass " + form.password_conf.data)
    #     if field.data != form.password_conf.data: 
    #         print("no match")
    #         raise ValidationError("Passwords don't match")
    #     print("match")
    #     return True
