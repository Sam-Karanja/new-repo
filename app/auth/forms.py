
from ast import Str
from importlib_metadata import email
from . import views,forms
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Enter your email address', validators=[DataRequired(),Email()])
    username = StringField('Enter your name',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired(),EqualTo('password_confirm',message = 'passwords must match')])
    password_confirm = PasswordField('Confirm password',validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField('Login')