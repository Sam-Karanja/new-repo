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
def user_loader(user_id):
    return User.query.get(int(user_id))



class Quotes:
    def __init__(self,author,id,quote):
        self.id=id
        self.author=author
        self.quote=quote

class User(db.Model,UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index=True)
    email = db.Column(db.String(255),unique=True,index=True)
    bio = db.Column(db.String(255))
    profile_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    posts = db.relationship('Post',backref='user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError("You can't read the password attribute")

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        self.pass_secure = generate_password_hash(password)


    def __repr__(self):
        return f'User{self.username}'

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer,primary_key=True)
    post_id = db.Column(db.Integer)
    post_title = db.Column(db.String)
    post_blog = db.Column(db.String)
    time_posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_posts(cls,id):
        posts = Post.query.filter_by(post_id = id).all()
        return posts