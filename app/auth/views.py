# -*- coding: utf-8 -*-
from app import mongo
from flask import flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from . import auth_bp


@auth_bp.route('/')
def home():
    if 'username' in session:
        username = session['username']
        return render_template('auth/index.html', username=username)
    return render_template('auth/index.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        doc = mongo.db.users.find_one({'username': username})
        hashed_password = doc.get('password')

        is_valid = check_password_hash(hashed_password, password)
        if is_valid:
            flash('Login successfully!')
            session['username'] = username
        else:
            flash('Login failed!')
        return redirect(url_for('auth.home'))
    return render_template('auth/login.html')


@auth_bp.route('/logout', methods=['GET'])
def logout():
    if 'username' in session:
        del session['username']

        flash('logout successfully!')
    return redirect(url_for('auth.home'))


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        mongo.db.users.insert_one({
            'username': username,
            'password': hashed_password,
        })

        flash('Sign up successfully!')
        return redirect(url_for('auth.home'))
    return render_template('auth/signup.html')
