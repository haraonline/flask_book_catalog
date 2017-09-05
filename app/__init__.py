# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_heroku import Heroku

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()
heroku = Heroku()


def create_app(config_type):  # dev, test, or prod

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    # C:\\Users\\dell\\PycharmProjects\\book_catalog\\config\\dev.py
    app.config.from_pyfile(configuration)
    db.init_app(app)  # initialize database
    bootstrap.init_app(app)  # initialize bootstrap
    login_manager.init_app(app)  # initialize login_manager
    bcrypt.init_app(app)
    heroku.init_app(app)

    from app.catalog import main  # import blueprint
    app.register_blueprint(main)  # register blueprint

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app
