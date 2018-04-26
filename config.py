
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
    AUTH_TOKEN = os.environ.get('AUTH_TOKEN')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lulumutuli:lulu@localhost/downtime'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  'postgresql+psycopg2://lulumutuli:lulu@localhost/downtime'
    SECRET_KEY='DOWNTIME2018'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_options ={"production":ProdConfig,"default":DevConfig}
