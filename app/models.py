from .import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime

'''
this decorator modifies the load_user funtion by passing user id that queries and 
gets a user with that Id
'''
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Quotes:
    def __init__(self,author,quote):
        self.author=author
        self.quote=quote

class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    posts = db.relationship('Post',backref='user',lazy = "dynamic")
    comment= db.relationship('Comment',backref='user',lazy='dynamic')


    @property
    def password(self):
        raise AttributeError("You can't read the password attribute")

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
       return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User{self.username}'


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String)
    time_posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref='Posts',lazy='dynamic')

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Post{self.body}'


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    post_id = db.Column(db.Integer,db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()

        return comments

    
    def __repr__(self):
        return f'comment:{self.comment}'