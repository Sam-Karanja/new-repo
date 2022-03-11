from os import abort
from flask import render_template,request,redirect,url_for
from.import main
from..request import get_quotes
from flask_login import login_required
from ..models import User
# Views


@main.route('/',methods=['GET','POST'])
@login_required
def index():

    '''
    View root page function that returns the index page and its data
    '''
    my_quote=get_quotes()

    message ="Quote for you. You are the best and nobody can change that"
    return render_template('index.html',message=message,quotes=my_quote)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    return render_template("profile/profile.html",user=user)
