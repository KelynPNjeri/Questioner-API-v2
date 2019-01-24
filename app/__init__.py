"""Creating an instance of app and create_app function."""
# Third party import
from flask import Flask, Response
from flask_jwt_extended import JWTManager

# Standard Library imports
import os
import json
from datetime import timedelta

# Local Import
from instance.config import APP_CONFIG
from .database import create_tables, initialize_db, drop_tables

def create_app(config_name):
    """Create App function."""
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    initialize_db()
    create_tables()

    
    #JWT Configurations.
    app.config["JWT_SECRET_KEY"] = 'mementomori'
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=6)
    app.config["JWT_BLACKLIST_ENABLED"] = True
    app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ['access']
    manager = JWTManager(app=app)

    # API Error Handlers.
    
    # JWT Error Handlers.
    @manager.token_in_blacklist_loader
    def check_if_token_is_blacklisted(decoded_token):
        pass

    @manager.unauthorized_loader
    def empty_token(msg):
        """Function dealing with """
        payload = dict(
            status=401,
            error="Missing token",
            message="Please enter a token"
        )
        resp = Response(json.dumps(payload), status=401, mimetype="application/json")
        return resp
 
    @manager.expired_token_loader
    def handling_expired_token():
        payload = dict(
            status=401,
            error="Token has expired.",
            message="Please log in."
        )
        resp= Response(json.dumps(payload), status=401, mimetype="application/json")
        return resp

    
    # Registering Blueprint
    from .api.v2 import version2 as v2
    from .api.v2 import api
    app.register_blueprint(v2)
    manager._set_error_handler_callbacks(api)

    # Adding Configurations.
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')

    return app
