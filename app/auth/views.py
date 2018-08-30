# -*- coding: utf-8 -*-
from flask import redirect, render_template, request, session, url_for

from . import auth_bp


@auth_bp.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return f'Hello, {username}'
    return f'Hello, friend!'


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('auth.home'))
    return render_template('auth/login.html')
