import os 

class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  'postgresql+psycopg2://kiptim:jerotich@localhost/downtime'
    SECRET_KEY=os.environ.get('DOWNTIME2018')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

config_options ={"production":ProdConfig,"default":DevConfig}

