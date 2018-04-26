from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from twilio.rest import Client
=======
from flask_login import LoginManager


login_manager = LoginManager()
login_manager.session_protection ='strong'
login_manager.login_view = 'auth.login'
>>>>>>> ad62fd7325d3f9ad7d7c50b22a52ca621befa050


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_state):
    app = Flask(__name__)

    app.config.from_object(config_options[config_state])

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix= '/authenticate')

    return app
