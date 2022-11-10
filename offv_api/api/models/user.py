# -*- coding: utf-8 -*-


from .. import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__( self, email, password, name ):
        self.email= emailf
        self.password = password
        self.name = name
