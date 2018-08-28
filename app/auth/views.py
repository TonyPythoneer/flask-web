# -*- coding: utf-8 -*-
from . import auth_bp


@auth_bp.route('/')
def show():
    return 'hello'


@auth_bp.route('/yoo')
def yoo():
    return 'yoo'
