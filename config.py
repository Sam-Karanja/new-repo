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
        SQLALCHEMY_DATABASE_URI =  'postgresql://ccqmtwcsfuniak:f75a2d81155a57f8d7241d46a6047cacf575b1e0016a9d22ecc306e49f940536@ec2-3-209-61-239.compute-1.amazonaws.com:5432/d4mqd75m3bjik9'
    #  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
        
  
   
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