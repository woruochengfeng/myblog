#!/usr/bin/env python3
# encoding: utf-8
# Author: Zhangxunan

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

app = Flask(__name__)
app.config.from_object(DevConfig)
db= SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __repr__(self):
        return "<User '{}'>".format(self.username)


@app.route('/')
def home():
    return '<h1>Hello ,Flask</h1>'


if __name__ == '__main__':
    app.run()