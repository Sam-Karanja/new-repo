from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Describe Yourself",validators=[DataRequired()])
    submit = SubmitField('Sumit')