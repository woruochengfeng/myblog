#!/usr/bin/env python3
# encoding: utf-8
# Author: Zhangxunan


class Config(object):
    pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
