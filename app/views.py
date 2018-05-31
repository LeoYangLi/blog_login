# coding=utf-8
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_required
from app import app


@app.route('/')
def app_main():
    return redirect(url_for('auth_bp.login'))

@app.route('/index')
@login_required  # 确保了这页面只被已经登录的用户看到
def index():
    user = {'name':'leo'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title = '',user = user,posts = posts)


@app.route('/file')
@login_required
def download_file():
    Column_list = ['id', 'name', 'password_hash', 'email']
    filename = BulidNewExcel(Column_list)


