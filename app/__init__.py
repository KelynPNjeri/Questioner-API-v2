"""Creating an instance of app and create_app function."""
# Third party import
from flask import Flask
from flask_jwt_extended import JWTManager

# Standard Library imports
import os
from datetime import timedelta

# Local Import
from instance.config import APP_CONFIG
from .database import create_tables, initialize_db

def create_app(config_name):
    """Create App function."""
    app = Flask(__name__, instance_relative_config=True)
    db = initialize_db(config_name=config_name)
    cursor = db.cursor()
    create_tables()

    manager = JWTManager(app=app)
    manager.init_app(app)
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config["JWT_BLACKLIST_ENABLED"] = True

    
    # Registering Blueprint
    from .api.v2 import version2 as v2
    app.register_blueprint(v2)

    # Adding Configurations.
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')


    
    return app
