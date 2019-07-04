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


class Roles(db.Model):
    __tablename__ = "roles"

    # unique identifier for a user
    id = db.Column(db.Integer, primary_key=True)
    # keyword of the role
    keyword = db.Column(db.String(80), unique=True)
    # description of the role
    description = db.Column(db.String(1000), nullable=True)

    # relationship variable, to list all the user_roles
    users = db.relationship('UserRoles', backref='enquiry', lazy=True)

    def __repr__(self):
        return '{"id": {0}, "keyword": {1}, "id": {2}, "description": {3} }'.format(self.id, self.keyword, self.id,
                                                                                    self.description)
