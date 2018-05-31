# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object('config')

bootstrap = Bootstrap()
bootstrap.init_app(app)

lm = LoginManager()
lm.init_app(app)

db = SQLAlchemy(app)

from app.auth import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from app import views, models