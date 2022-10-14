# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS', "api.config.DevelopmentConfig"))
    app.config['SECRET_KEY'] = 'yuibgnq98rycp8tybiytwa'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    from .routes import register_routes
    register_routes( app )

    from .models import User, Result
    migrate = Migrate(app, db)

    return app
