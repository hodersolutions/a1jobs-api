##########################################################################
# Name: main
# Purpose: main module which creates the Application instance
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import DefaultConfig

cors = CORS()
db = SQLAlchemy()
jwt = JWTManager()


def create_app(config_class=DefaultConfig):
    """
    Creates the app instance with its own config and other values.
    :param config_class:
    :return: app instance
    """
    app = Flask(__name__)
    # we need a .config file to store these values not a python class TODO
    app.config.from_object(DefaultConfig)

    db.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)

    from logins.routes import logins
    from main.routes import main
    from services.users.routes import users

    app.register_blueprint(logins)
    app.register_blueprint(main)
    app.register_blueprint(users)

    return app
