##########################################################################
# Name:     Users
# Purpose: File contains Users
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db
from passlib.hash import pbkdf2_sha256 as sha256
from datetime import datetime, timedelta


class Users(db.Model):
	__tablename__ = "users"

	# unique identifier for a user, todo: need to have uuid or mobile as unique identifier
	id = db.Column(db.Integer, primary_key=True)
	# first name of a user
	first_name = db.Column(db.String(80), nullable=True)
	# last name of a user
	last_name = db.Column(db.String(80), nullable=True)
	# email of the user, cannot be null, and should be unique
	email = db.Column(db.String(80), nullable=True)
	# mobile number of the user
	mobile = db.Column(db.String(80), nullable=True)
	# decrypted value
	password = db.Column(db.String(80), nullable=False)
	# registration time
	registered_on = db.Column(db.DateTime, nullable=False, default=datetime.now())
	# If user is not with the Org anymore, TODO: use this effectively
	is_active = db.Column(db.Boolean, nullable=False, default=False)

	# foreign key from the user_roles table
	# roles = db.relationship('UserRoles', backref='enquiry', lazy=True)

	def __repr__(self):
		return "{ email: {1}, id: {2}, mobile: {3} }".format(self.email, self.id, self.mobile)

	def fullname(self):
		return "{} {}".format(self.first_name, self.last_name)

	@staticmethod
	def generate_hash(password):
		return sha256.hash(password)

	@staticmethod
	def verify_hash(password, hash):
		return sha256.verify(password, hash)

	@classmethod
	def add_user(cls, _user):
		try:
			pw_hash = cls.generate_hash(_user.password)
			_user.password = pw_hash
			db.session.add(_user)
			# add the role to the user before the db commit
			# user_roles.UserRoles.add_user_role(_user.id, _role)
			db.session.commit()
		except Exception as e:
			return None, e

		return cls.get_user_by_email(_user.email), None

	@classmethod
	def get_all_users(cls):
		return [user.serialize() for user in cls.query.all()]

	@classmethod
	def get_user_by_email(cls, _email):
		try:
			user_object = cls.query.filter_by(email=_email).first()
			if not user_object:
				return user_object
			else:
				return user_object.serialize()
		except:
			return None

	@classmethod
	def get_users_from_text(cls, text):
		query = """select id, Users.firstname, Users.lastname from Users where Users.firstname like "%{}%"
		 or Users.lastname like "%{}%" or Users.username like "%{}%" """.format(text, text, text)
		result = db.engine.execute(query)
		list_result =[]
		for user in result:
			user_dict = {}
			user_dict['id'] = user[0]
			user_dict['label'] = "{} {}".format(user[1], user[2])
			list_result.append(user_dict)
		return list_result

	@classmethod
	def get_user_by_id(cls, id):
		user_object = cls.query.get(id)
		if not user_object:
			return None
		else:
			return user_object

	@classmethod
	def delete_user_by_username(cls, _username):
		try:
			cls.query.filter_by(username=_username).delete()
			db.session.commit()
		except:
			return False

		return True


	@classmethod
	def update_user_by_username(cls, _username, _user):
		try:
			user_to_update = cls.query.filter_by(username=_username).first()
			user_to_update.email = _user.email
			user_to_update.password = _user.password
			db.session.commit()
		except:
			return False

		return cls.get_user_by_username(_user.username)

	def encode_auth_token(self):
		"""
		Generates the Auth Token
		:return: string
		"""
		try:
			header = {
				"alg": "HS256",
				"typ": "JWT"
			}
			# Max value = timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)
			payload = {
				"exp": datetime.utcnow() + timedelta(days=2, hours=0, minutes=0, seconds=0, microseconds=0),
				"iat": datetime.utcnow(),
				"sub": self.id,
				"email": self.email
			}
			return encode(payload, self.email, headers=header)
		except Exception as e:
			return e

	@classmethod
	def get_users_by_filter(cls, filter):
		query = "select * from Users inner join seekerdetails on Users.id = Seekerdetails.user where "
		for key, value in filter.items():
			query = "{} Seekerdetails.{} = {}".format(query, key, value)
		print(query)
		result = db.engine.execute(query)
		list_result =[]
		for job in result:
			job_object = dict(zip(result.keys(), job))
			list_result.append(cls.serialize_dict(job_object))

		return list_result

	def serialize(self):
		json_user = {
			"id": self.id,
			"mobile": self.mobile,
			"Email": self.email,
			#"registered_on": str(self.registered_on),
			"Fullname": self.fullname(),
		}
		return json_user

############################################################################################
# All the functions to retrieve seeker details and update them
############################################################################################
	def update_user(self):
		db.session.add(self)
		db.session.commit()
