from crypt import methods
from os import abort
from flask import render_template,request,redirect,url_for
from.import main
from..request import get_quotes
from flask_login import current_user, login_required
from ..models import Post, Quotes, User
from .forms import UpdateProfile,PostForm
from ..import db,photos

@main.route('/',methods = ['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    my_quote=get_quotes()
    post=Post.query.all()
    message ="Quote for you. You are the best and nobody can change that"
    return render_template('index.html',message=message,quotes=my_quote,post=post)

@main.route('/new_post', methods=['GET', 'POST'])
def post():
    
    form = PostForm()
    if current_user.is_authenticated and \
        form.validate_on_submit():
        post = Post(post_blog=form.post_blog.data,
        author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.post'))
    posts = Post.query.order_by(Post.time_posted.desc()).all()
    return render_template('post.html', form=form, posts=posts)



@main.route('/user/<uname>/update')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html",user = user) 


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first() 

    if user is None:
        abort(404)
    form = UpdateProfile()
    
    if form.validate_on_submit():
        user.bio(form.bio.data)
        db.session.add(user)
        db.session.commit()
    return render_template("profile/update.html", form = form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
