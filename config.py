import os

from flask import config


class Config:
    
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