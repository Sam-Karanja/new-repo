from flask import redirect, render_template, url_for,flash,request
from ..models import Post, User
from .forms import LoginForm, RegistrationForm
from flask_login import login_required, login_user, logout_user
from . import auth
from ..import db
from .. email import mail_message
@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        mail_message("Welcom to one minute pitch","email/welcome_user",user.email)
        return redirect(url_for('auth.login'))
        title = "New Account"
    return render_template('auth/register.html',registration_form = form)

@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if request.method=='POST':
        print("method POST*******************************************")
        if login_form.validate_on_submit():
            user = User.query.filter_by(email = login_form.email.data).first()
            print(user.email+"****************************")
            print(user.verify_password (login_form.password.data))
            if user is not None and user.verify_password(login_form.password.data):
               
                login_user(user,login_form.remember_me.data)
                print("login************************************")
                return redirect(url_for('main.index'))
                # return redirect(request.args.get('next') or url_for('main.index'))

            flash('Invalid username or Password')

    title = "blog login"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))




