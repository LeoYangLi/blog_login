# coding=utf-8
from app import db
from flask_login import login_manager
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120))
    post = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode()
        except NameError:
            return str(self.id)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.name)


class Post(db.Model):
    __tablename__ = 'Post'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1200))
    timestamp = db.Column(db.DATETIME)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    def __repr__(self):
        return '<Post %r>' % (self.body)

#@login_manager.LoginManager.user_loader
#def load_user(user_id):
#    return User.query.get(int(user_id))