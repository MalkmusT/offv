# -*- coding: utf-8 -*-


def register_routes( app ):
    # blueprint for auth routes in our app
    from api.routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from api.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

