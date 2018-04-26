
import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
    AUTH_TOKEN = os.environ.get('AUTH_TOKEN')



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI =  os.environ.get('DATABASE_URL')

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  'postgresql+psycopg2://lulumutuli:lulu@localhost/downtime'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_options ={"production":ProdConfig,"default":DevConfig}
