#!/usr/bin/env python3
# encoding: utf-8
# Author: Zhangxunan

from flask_script import Manager, Server
from main import app, db, User, Post, Comment


manager = Manager(app)
manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Post=Post, Comment=Comment)


if __name__ == '__main__':
    manager.run()