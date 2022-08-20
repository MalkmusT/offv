import os
import time

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.getenv( 'APP_SETTINGS', "config.DevelopmentConfig"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from models import Result


# Routes starting here

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}
@app.route('/api/search/<term>')
def get_search_result():
    return { 'results' : [ 
    { 'id' : 1, 'text' : 'AA' }, 
    { 'id' : 2, 'text' : 'AB' }, 
    { 'id' : 3, 'text' : 'BB' },
    ] }
