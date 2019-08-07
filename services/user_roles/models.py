##########################################################################
# Name:     Roles
# Purpose: File contains Roles
# Roles by default can be the following and a user can have multiple roles, eg: SuperAdmin and Principal
# 	1. Super Admin
# 	2. Management / Board Members
# 	3. Principal
# 	4. Staff / Teacher
# 	5. Student
#  	6. Parent / Guardian
#   we can add more roles to the Roles table, for eg: security
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db


class UserRoles(db.Model):
    __tablename__ = "user_roles"

    user = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    role = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)

    # dangerous, infinite loop possible
    # users = db.relationship('Users', backref='enquiry', lazy=True)
    # relationship variable, to list all the user_roles
    roles = db.relationship('Roles', backref='enquiry', lazy=True)

    def __repr__(self):
        return '{"user": {0}, "role": {1}}'.format(self.user.Fullname(), self.role.description)

    @classmethod
    def add_user_role(cls, _user_role):
        try:
            db.session.add(_user_role)
            db.session.commit()
        except Exception as e:
            return {'msg': e}

        return None

    @classmethod
    def delete_user_role(cls, _user_role):
        try:
            db.session.add(_user_role)
            db.session.commit()
        except Exception as e:
            return {'msg': e}

        return None

    @classmethod
    def update_user_role(cls, _user_role):
        try:
            db.session.commit()
        except Exception as e:
            return {'msg': e}

        return None