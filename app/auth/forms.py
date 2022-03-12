from flask_wtf import FlaskForm
from importlib_metadata import email
from wtforms import StringField,PasswordField,SubmitField,BooleanField,ValidationError
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Enter your email address', validators=[DataRequired(),Email()])
    username = StringField('Enter your name',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired(),EqualTo('password_confirm',message = 'passwords must match')])
    password_confirm = PasswordField('Confirm password',validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('That email is already used')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError("Username already exist")

class LoginForm(FlaskForm):
    email = StringField("Email Address", validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField('Login')


