# -*- coding: utf-8 -*-
from app import create_app, init_app
from flask_pymongo import PyMongo

app = create_app()
app = init_app(app)

mongo = PyMongo(app, uri='mongodb://mongodb:27017/myDatabase')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
