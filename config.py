import os

from flask import config


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blogs'
    SECRET_KEY = 'SECRET_KEY'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    '''
    contains configurations used in bothe development and production stages
    '''


class ProdConfig(Config):
    '''
    '''


class DevConfig(Config):
    '''
    
    '''
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}