import os

from flask import config


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234@localhost/blogs'
    '''
    contains configurations used in bothe development and production stages
    '''
    pass

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