from os import abort
from flask import render_template,request,redirect,url_for,session
from.import main
from..request import get_quotes
from flask_login import current_user, login_required
from ..models import Post, User,Comment
from .forms import UpdateProfile,PostForm,CommentForm
from ..import db,photos

@main.route('/',methods = ['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    my_quote=get_quotes()
    posts=Post.query.all()
    comments=Comment.query.all()
    message ="Quote for you. You are the best and nobody can change that"
    return render_template('index.html',message=message,quotes=my_quote,posts=posts,comments=comments)

@main.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
            post = Post(body=form.body.data,user_id=current_user.id)
            post.save_post()
            return redirect(url_for('main.index'))
    posts = Post.query.order_by(Post.time_posted.desc()).all()
    return render_template('post.html', form=form,posts=posts)

@main.route('/comment/<post_id>', methods = ['POST','GET'])
@login_required
def comment(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(comment=form.comment.data,user_id=current_user.id)
        comment.save_comment()
        return redirect(url_for('.comment', post_id = post_id))
    comments =  comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template('comment.html', form =form,comments=comments)


@main.route('/user/<uname>')
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
        return redirect(url_for('.profile',uname=user.username))
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
