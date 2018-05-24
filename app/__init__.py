# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import basedir
import os

app = Flask(__name__)
app.config.from_object('config')
bootstrap = Bootstrap()
bootstrap.init_app(app)
lm = LoginManager()
lm.init_app(app)
db = SQLAlchemy(app)
from app import views, models