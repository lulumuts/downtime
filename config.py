import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    account_sid = 'AC905360593c371acea0ec4417770b3fd5'
    auth_token = 'd962e83a5a6c92b72a2530e705db61eb'

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://levi:eyeshadow@localhost/downtime'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}
