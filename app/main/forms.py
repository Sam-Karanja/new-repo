
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField("Describe Yourself",validators=[DataRequired()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    '''
    '''
    body = TextAreaField("input your personal blog here",validators=[DataRequired()])
    submit= SubmitField("Submit")

class CommentForm(FlaskForm):
    
    comment = TextAreaField('Add a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')