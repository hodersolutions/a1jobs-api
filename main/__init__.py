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


application = Flask(__name__)
# we need a .config file to store these values not a python class TODO
application.config.from_object(DefaultConfig)

cors = CORS(application)
db = SQLAlchemy(application)
jwt = JWTManager(application)


from attributes.reservations.routes import reservations
from attributes.religions.routes import religions
from attributes.subjects.routes import subjects
from attributes.institutions.routes import institutions
from attributes.towns.routes import towns
from attributes.districts.routes import districts
from attributes.states.routes import states
from attributes.jobtypes.routes import jobtypes
from attributes.qualifications.routes import qualifications
from logins.routes import logins
from config.routes import config
from main.routes import main
from services.requisitions.routes import requisitions
from services.submissions.routes import jobapplications

application.register_blueprint(config)
application.register_blueprint(logins)
application.register_blueprint(main)
application.register_blueprint(reservations)
application.register_blueprint(religions)
application.register_blueprint(subjects)
application.register_blueprint(jobtypes)
application.register_blueprint(institutions)
application.register_blueprint(towns)
application.register_blueprint(districts)
application.register_blueprint(states)
application.register_blueprint(qualifications)
application.register_blueprint(requisitions)
application.register_blueprint(jobapplications)