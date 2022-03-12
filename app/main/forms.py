
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Describe Yourself",validators=[DataRequired()])
    submit = SubmitField('Sumit')

class PostForm(FlaskForm):
    '''
    '''
    post_blog = TextAreaField("input your personal blog here",validators=[DataRequired()])
    submit= SubmitField("save")