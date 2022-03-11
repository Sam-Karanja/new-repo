from flask import redirect, render_template, url_for,flash,request
from ..models import User
from .forms import LoginForm, RegistrationForm
from flask_login import login_required, login_user, logout_user
from . import auth
from ..import db


@auth.route('/register',methods = ["GET","POST"])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        user = User (email = form.email.data,username=form.username.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',reg_form=form)


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user=User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            # return redirect(url_for("main.index"))
            return redirect(request.args.get('next')or url_for('main.index'))
        flash("Invalid credentials")
    return render_template('auth/login.html',login_form = login_form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
