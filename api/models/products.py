# -*- coding: utf-8 -*-


from api import db
from sqlalchemy.dialects.postgresql import JSON

class Incredient (db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100), unique=True)
    def __init__( self, id, name ):
        self.id = id
        self.name = name 


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100), unique=True)
    incredients = db.Column(db.String(100))

    def __init__( self, id, name, incredients ):
        self.id = id
        self.name = name
        self.incredients = incredients




def register_incredient(inc):
    entry = Incredient(  inc['name'] )
    db.session.add( entry )
    db.session.commit()
    return entry.id


def register_product(prod):
    inc_ids = []
    for inc in prod['ingredients']:
        can = Incredient.query.filter(inc['name']).first()
        if can :
            inc_ids.append(can.id)
        else:
            inc_ids.append(register_incredient(inc))

    entry = Product( product['name'], inc_ids )
    db.session.add(entry)
    db.sesion.commit()
    return entry.id
