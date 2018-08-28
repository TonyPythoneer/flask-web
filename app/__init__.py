# -*- coding: utf-8 -*-
"""Init flask app
"""

from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    return app


def init_app(app: Flask) -> Flask:
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    return app
