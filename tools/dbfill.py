##########################################################################
# Name:     database creator
# Purpose: File contains the db creation and filling of the required attributes
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db
import pandas as pd
from attributes.districts.models import Districts
from attributes.institutions.models import Institutions
from attributes.religions.models import Religions
from attributes.reservations.models import Reservations
from attributes.standards.models import Standards
from attributes.qualifications.models import Qualifications
from attributes.states.models import States
from attributes.subjects.models import Subjects
from attributes.towns.models import Towns
from attributes.roles.models import Roles
from attributes.jobtypes.models import JobTypes
from logins.models import Users


# Fill the districts
def fill_districts():
	if len(Districts.query.all()) > 0:
		return
	df = pd.read_json('./tools/data/ap_districts.json')	
	df.index.rename("id", inplace=True)
	df.to_sql(name='districts', if_exists='append', con=db.engine)

# Fill the jobtypes
def fill_job_types():
	if len(JobTypes.query.all()) > 0:
		return
	df = pd.read_json('./tools/data/job_types.json')	
	df.index.rename("id", inplace=True)
	df.to_sql(name='job_types', if_exists='append', con=db.engine)

# Fill the qualifications
def fill_qualifications():
	if len(Qualifications.query.all()) > 0:
		return
	df = pd.read_json('./tools/data/qualifications.json')
	df.index.rename("id", inplace=True)
	df.to_sql(name='qualifications', if_exists='append', con=db.engine)

# Fill the towns
def fill_towns():
	if len(Towns.query.all()) > 0:
		return
	df = pd.read_json('./tools/data/ap_towns.json')	
	df.index.rename("id", inplace=True)
	df.to_sql(name='towns', if_exists='append', con=db.engine)

# Fill the states
def fill_states():
	if len(States.query.all()) > 0:
		return
	df = pd.read_json('./tools/data/states.json')	
	df.index.rename("id", inplace=True)
	df.to_sql(name='states', if_exists='append', con=db.engine)

# Fill the institutions
def fill_institutions():
	if len(Institutions.query.all()) > 0:
		return
	df = pd.read_json('./tools/data/institutions.json')	
	df.index.rename("id", inplace=True)
	df.to_sql(name='institutions', if_exists='append', con=db.engine)

# Fill the subjects
def fill_subjects():
	if len(Subjects.query.all()) > 0:
		return
	df = pd.read_json('./tools/data/subjects.json')	
	df.index.rename("id", inplace=True)
	df.to_sql(name='subjects', if_exists='append', con=db.engine)

# Fill the standards
# def fill_standards():
# 	if len(Standards.query.all()) > 0:
# 		return
# 	df = pd.read_json('./tools/data/standards.json')
# 	df.index = range(1, len(df) + 1)
# 	df.index.rename("id", inplace=True)
# 	df.to_sql(name='standards', if_exists='append', con=db.engine)

# Fill the reservations
def fill_reservations():
	if len(Reservations.query.all()) > 0:
		return
	df = pd.read_json('./tools/data/reservations.json')
	df.index.rename("id", inplace=True)
	df.to_sql(name='reservations', if_exists='append', con=db.engine)

# Fill the religions
def fill_religions():
	if len(Religions.query.all()) > 0:
		return
	df = pd.read_json('./tools/data/religions.json')
	df.index.rename("id", inplace=True)
	df.to_sql(name='religions', if_exists='append', con=db.engine)

# Fill the roles
# def fill_roles():
# 	if len(Roles.query.all()) > 0:
# 		return
# 	df = pd.read_json('./tools/data/roles.json')
# 	df.index = range(1, len(df) + 1)
# 	df.index.rename("id", inplace=True)
# 	df.to_sql(name='roles', if_exists='append', con=db.engine)

# Fill the users
def fill_users():
	if len(Users.query.all()) > 0:
		return
	df = pd.read_json('./tools/data/users.json')
	df.index.rename("id", inplace=True)
	df.to_sql(name='users', if_exists='append', con=db.engine)

# Fill the user roles
# def fill_user_roles():
# 	if len(UserRoles.query.all()) > 0:
# 		return
# 	df = pd.read_json('./tools/data/user_roles.json')
# 	df.index = range(1, len(df) + 1)
# 	df.to_sql(name='user_roles', if_exists='append', con=db.engine, index=False)