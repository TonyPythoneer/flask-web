# -*- coding: utf-8 -*-
class BaseConfig(object):
    """
    Flask config
    ref: http://flask.pocoo.org/docs/1.0/config/
    """
    # custom server settings
    HOST = '0.0.0.0'

    # env settings
    ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = '_5#y2L"F4Q8z\n\xec]/'

    # db settings
    MONGO_URI = 'mongodb://mongodb:27017/myDatabase'
