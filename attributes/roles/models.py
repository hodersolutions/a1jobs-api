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
    keyword = db.Column(db.String(80), nullable=False)
    # description of the role
    description = db.Column(db.String(1000), nullable=True)

    # relationship variable, to list all the user_roles
    # role_users = db.relationship('UserRoles', backref='enquiry', lazy=True)

    def __repr__(self):
        return '{"id": {0}, "keyword": {1}, "id": {2}, "description": {3} }'.format(self.id, self.keyword, self.id,
                                                                                    self.description)

    @classmethod
    def get_role(cls, _keyword):
        """
        currently we are getting the values hardcoded
        TODO: get the keyword->id values from database
        :param keyword:
        :return:
        """
        try:
            role = cls.query.filter_by(keyword=_keyword).first()
            if not role:
                return None
            else:
                return role.serialize()
        except:
            return None

    @classmethod
    def add_role(cls, _role):
        """
        currently we are getting the values hardcoded
        TODO: get the keyword->id values from database
        :param keyword: _role
        :return:
        """
        try:
            db.session.add(_role)
            db.session.commit()
        except Exception as e:
            return {'msg': e}

        return _role

    @classmethod
    def get_all_roles(cls):
        return [roles.serialize() for roles in cls.query.all()]

    def serialize(self):
        json_role = {
            "id": self.id,
            "keyword": self.keyword,
            "description": self.description,
            # "users": [role_user.users.serialize_without_role() for role_user in self.role_users]
        }
        return json_role

    def serialize_without_users(self):
        json_role = {
            "id": self.id,
            "keyword": self.keyword,
            "description": self.description,
        }
        return json_role

