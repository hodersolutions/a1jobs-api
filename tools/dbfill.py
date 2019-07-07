from main import db
import pandas as pd


# Fill the districts
def fill_districts():
	df = pd.read_json('./tools/ap_districts.json')
	df.index = range(1, len(df) + 1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='districts', if_exists='append', con=db.engine)


# Fill the towns
def fill_towns():
	df = pd.read_json('./tools/ap_towns.json')
	df.index = range(1, len(df) + 1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='towns', if_exists='append', con=db.engine)


# Fill the districts
def fill_states():
	df = pd.read_json('./tools/states.json')
	df.index = range(1, len(df) + 1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='states', if_exists='append', con=db.engine)


def fill_institutions():
	df = pd.read_json('./tools/institutions.json')
	df.index = range(1, len(df) + 1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='institutions', if_exists='append', con=db.engine)


def fill_subjects():
	df = pd.read_json('./tools/subjects.json')
	df.index = range(1, len(df) + 1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='subjects', if_exists='append', con=db.engine)


def fill_standards():
	df = pd.read_json('./tools/standards.json')
	df.index = range(1, len(df) + 1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='standards', if_exists='append', con=db.engine)


def fill_castes():
	df = pd.read_json('./tools/castes.json')
	df.index = range(1, len(df) + 1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='castes', if_exists='append', con=db.engine)


def fill_religions():
	df = pd.read_json('./tools/religions.json')
	df.index = range(1, len(df) + 1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='religions', if_exists='append', con=db.engine)


def fill_roles():
	df = pd.read_json('./tools/roles.json')
	df.index = range(1, len(df) + 1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='roles', if_exists='append', con=db.engine)


def fill_users():
	df = pd.read_json('./tools/users.json')
	df.index = range(1, len(df) + 1)
	df.index.rename("id", inplace=True)
	df.to_sql(name='users', if_exists='append', con=db.engine)


def fill_user_roles():
	df = pd.read_json('./tools/user_roles.json')
	df.index = range(1, len(df) + 1)
	df.reset_index(drop=True, inplace=True)
	df.to_sql(name='user_roles', if_exists='append', con=db.engine)

