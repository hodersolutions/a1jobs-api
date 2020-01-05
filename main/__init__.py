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


app = Flask(__name__)
# we need a .config file to store these values not a python class TODO
app.config.from_object(DefaultConfig)

cors = CORS(app)
db = SQLAlchemy(app)
jwt = JWTManager(app)


from attributes.reservations.routes import reservations
from attributes.religions.routes import religions
from attributes.subjects.routes import subjects
from attributes.institutions.routes import institutions
from attributes.towns.routes import towns
from attributes.districts.routes import districts
from attributes.states.routes import states
from attributes.jobtypes.routes import jobtypes
from logins.routes import logins
from config.routes import config
from main.routes import main
from services.requisitions.routes import requisitions
from services.submissions.routes import jobapplications

app.register_blueprint(config)
app.register_blueprint(logins)
app.register_blueprint(main)
app.register_blueprint(reservations)
app.register_blueprint(religions)
app.register_blueprint(subjects)
app.register_blueprint(jobtypes)
app.register_blueprint(institutions)
app.register_blueprint(towns)
app.register_blueprint(districts)
app.register_blueprint(states)
app.register_blueprint(requisitions)
app.register_blueprint(jobapplications)