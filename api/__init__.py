import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(app, db)

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS', "api.config.DevelopmentConfig"))
    app.config['SECRET_KEY'] = 'yuibgnq98rycp8tybiytwa'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from models import Result

    return app
