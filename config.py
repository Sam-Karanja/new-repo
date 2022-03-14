import os
from pickle import TRUE
from flask import config


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blogs'
    SECRET_KEY = 'SECRET_KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'blogs'
    SENDER_EMAIL = 'melodytowett99@gmail.com'

    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_IIFE = True

    @staticmethod
    def init_app(app):
        pass
    '''
    contains configurations used in bothe development and production stages
    '''


class ProdConfig(Config):
    #    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    #  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
       SQLALCHMEY_DATABASE_URI = ' postgresql://emsjojwnuougdr:46ca9d2bdfafeef5dd0d1d17bf8a4636803ccd50ff0e27fe8439cde35599bac4@ec2-54-198-252-9.compute-1.amazonaws.com:5432/ddjkikfboajcnc'
  
  
   
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blog_test'
    '''
    '''

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blogs'

    '''
    
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}