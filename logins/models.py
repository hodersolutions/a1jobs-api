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
from datetime import datetime


class UserLogin(db.Model):
    __tablename__ = "user_login"

    # unique identifier for a user, todo: need to have uuid or mobile as unique identifier
    id = db.Column(db.Integer, primary_key=True)
    # email of the user, cannot be null, and should be unique
    email = db.Column(db.String(80), nullable=True)
    # mobile number of the user
    mobile = db.Column(db.String(80), nullable=True)
    # decrypted value
    password = db.Column(db.String(80), nullable=False)
    # registration time
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.now())
    # If user is not with the Org anymore, TODO: use this effectively
    is_active = db.Column(db.Boolean, nullable=False, default=True)

    # foreign key from the user_roles table
    # roles = db.relationship('UserRoles', backref='enquiry', lazy=True)

    def __repr__(self):
        return "{ email: {1}, id: {2}, mobile: {3} }".format(self.email, self.id, self.mobile)

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
            _user.is_active = 1
            db.session.add(_user)
            # add the role to the user before the db commit
            # user_roles.UserRoles.add_user_role(_user.id, _role)
            db.session.commit()
        except Exception as e:
            return None, e

        return cls.get_user_by_email(_user.email), None


    @classmethod
    def get_user_by_email(cls, _email):
        try:
            user_object = cls.query.filter_by(email=_email).first()
            return user_object
        except:
            return None

    @classmethod
    def get_user_by_mobile(cls, _mobile):
        try:
            user_object = cls.query.filter_by(mobile=_mobile).first()
            return user_object
        except:
            return None

    @classmethod
    def get_user_by_id(cls, id):
        user_object = cls.query.get(id)
        if not user_object:
            return None
        else:
            return user_object

    def serialize(self):
        json_user = {
            "id": self.id,
            "mobile": self.mobile,
            "Email": self.email
            #"registered_on": str(self.registered_on),
        }
        return json_user

############################################################################################
# All the functions to retrieve seeker details and update them
############################################################################################
    def update_user(self):
        db.session.add(self)
        db.session.commit()
