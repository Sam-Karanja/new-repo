import os

from flask import config


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blogs'
    SECRET_KEY = 'SECRET_KEY'

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