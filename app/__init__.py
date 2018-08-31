# -*- coding: utf-8 -*-
"""Init flask app
"""
from .settings import Config
from flask import Flask
from flask_pymongo import PyMongo


mongo = PyMongo()


def create_app() -> Flask:
    # Init flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    mongo.init_app(app, uri=Config.MONGO_URI)

    # Init blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    return app
