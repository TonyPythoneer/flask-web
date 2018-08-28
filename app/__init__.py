# -*- coding: utf-8 -*-
"""Init flask app
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    return app
