##########################################################################
# Name:     UserRoles
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

    user = db.Column(db.Integer, db.ForeignKey('user_login.id'), primary_key=True)
    role = db.Column(db.Integer, db.ForeignKey('roles.id'), primary_key=True)

    def __repr__(self):
        return '{"user": {0}, "role": {1}}'.format(self.user.Fullname(), self.role.description)

    @classmethod
    def add_user_role(cls, _user, _role):
        try:
            db.session.add(UserRoles(user=_user, role=_role))
        except Exception as e:
            return {'msg': e}

        return None
