import os

class Config(object):
    """docstring for Config"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'oh my gosh this string is so hard to guess'