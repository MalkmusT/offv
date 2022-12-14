# -*- coding: utf-8 -*-


from flask import Blueprint 
from api import db, create_app

from api.models import Result, User

import time

main = Blueprint('main', __name__)

# Routes starting here

@main.route('/api/time')
def get_current_time():
    return {'time': time.time()}

@main.route('/api/search/<term>')
def get_search_result(term):
    Result.query.all()
    return { 'results' : [ 
    { 'id' : 1, 'text' : 'AA' }, 
    { 'id' : 2, 'text' : 'AB' }, 
    { 'id' : 3, 'text' : 'BB' },
    ] }
