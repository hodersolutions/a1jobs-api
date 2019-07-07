##########################################################################
# Name:     Users
# Purpose: File contains User details of all the members in the Org
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db
from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256


class Users(db.Model):
    __tablename__ = "users"

    # unique identifier for a user
    id = db.Column(db.Integer, primary_key=True)
    # uid, can be student's enrollment id, staff's employee_id
    uid = db.Column(db.Integer, nullable=False)
    # institute id
    uid = db.Column(db.Integer, nullable=False)
    # encrypted value
    password = db.Column(db.String(200), nullable=True)
    # first name of a user
    first_name = db.Column(db.String(80), nullable=True)
    # last name of a user
    last_name = db.Column(db.String(80), nullable=True)
    # email of the user, cannot be null, and should be unique
    email = db.Column(db.String(80), nullable=True)
    # mobile number of the user
    mobile = db.Column(db.String(80), nullable=True)
    # registration time
    creation_date = db.Column(db.DateTime, nullable=True, default=datetime.now())
    # If user is not with the Org anymore, TODO: use this effectively
    is_active = db.Column(db.Boolean, nullable=True, default=1)
    # user who is enrolling this record
    user_creator = db.Column(db.Integer, nullable=True)
    # user who is updating this record
    user_modifier = db.Column(db.Integer, nullable=True)
    # json value to store user specific details
    details = db.Column(db.String(2000), nullable=True)

    # foreign key from the user_roles table
    # roles_list = db.relationship('UserRoles', backref='enquiry', lazy=True)

    # foreign key from the user_details table
    # roles = db.relationship('UserDetails', backref='enquiry', lazy=True)

    def __repr__(self):
        return "{ email: {1}, id: {2}, mobile: {3} }".format(self.email, self.id, self.mobile)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    @classmethod
    def add_user(cls, _user):
        try:
            # pw_hash = cls.generate_hash(_user.password)
            # _user.password = pw_hash
            # _user.is_active = 1
            db.session.add(_user)
            # add the role to the user before the db commit
            # user_roles.UserRoles.add_user_role(_user.id, _role)
            db.session.commit()
        except Exception as e:
            return None, e

        return cls.get_user_by_uid(_user.uid), None

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
    def get_user_by_uid(cls, _uid):
        try:
            user_object = cls.query.filter_by(uid=_uid).first()
            if not user_object:
                return user_object
            else:
                return user_object
        except:
            return None

    @classmethod
    def get_users_from_text(cls, text):
        query = """select id, Users.firstname, Users.lastname from Users where Users.firstname like "%{}%"
        or Users.lastname like "%{}%" or Users.username like "%{}%" """.format(text, text, text)
        result = db.engine.execute(query)
        list_result = []
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
    def delete_user_by_uid(cls, _uid):
        try:
            cls.query.filter_by(uid=_uid).delete() # todo: use is_active instead of deleting the record
            db.session.commit()
        except:
            return False

        return True

    @classmethod
    def update_user_by_email(cls, _email, _user):
        try:
            user_to_update = cls.query.filter_by(email=_email).first()
            user_to_update.email = _user.email
            db.session.commit()
        except:
            return False

        return cls.get_user_by_email(_user.email)

    def serialize(self):
        json_user = {
            "id": self.id,
            "uid": self.uid,
            "mobile": self.mobile,
            "Email": self.email,
            # "registered_on": str(self.registered_on),
            "Fullname": self.fullname(),
            "details": self.details
        }
        return json_user

    ############################################################################################
    # All the functions to retrieve seeker details and update them
    ############################################################################################
    def update_user(self):
        db.session.add(self)
        db.session.commit()
        return True, False


class UsersAudit(db.Model):
    __tablename__ = "users_audit"

    # unique identifier for a user
    audit_id = db.Column(db.Integer, primary_key=True)
    # user identifier
    id = db.Column(db.Integer, nullable=False)
    # uid, can be student's enrollment id, staff's employee_id
    uid = db.Column(db.Integer, nullable=False)
    # encrypted value
    password = db.Column(db.String(200), nullable=True)
    # first name of a user
    first_name = db.Column(db.String(80), nullable=True)
    # last name of a user
    last_name = db.Column(db.String(80), nullable=True)
    # email of the user, cannot be null, and should be unique
    email = db.Column(db.String(80), nullable=True)
    # mobile number of the user
    mobile = db.Column(db.String(80), nullable=True)
    # registration time
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    # If user is not with the Org anymore, TODO: use this effectively
    is_active = db.Column(db.Boolean, nullable=True, default=1)
    # user who is enrolling this record
    user_creator = db.Column(db.Integer, nullable=True)
    # user who is updating this record
    user_modifier = db.Column(db.Integer, nullable=True)
    # json value to store user specific details
    details = db.Column(db.String(2000), nullable=True)