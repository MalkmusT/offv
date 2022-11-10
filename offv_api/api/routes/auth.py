# -*- coding: utf-8 -*-

from flask import Blueprint 
from offv import db

auth = Blueprint('auth', __name__)

# Routes starting here

@auth.route('/api/login')
def login():
    return 'Login'

@auth.route('/api/logout')
def logout():
    return 'logout'

@auth.route('/api/sign_up')
def sgin_up():
    return 'sign-up'


