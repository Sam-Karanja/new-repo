from flask import redirect, render_template, url_for
from ..models import User
from .forms import RegistrationForm
from . import auth
from ..import db


@auth.route('/register',methods = ["GET","POST"])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        user = User (emali = form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',reg_form=form)


@auth.route('/login')
def login():
    return render_template('auth/login.html')
