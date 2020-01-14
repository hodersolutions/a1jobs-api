##########################################################################
# Name:     JobTypes
# Purpose: File contains JobTypes
# 	1. Freelance
# 	2. Fulltime
# 	3. Parttime
#
# Author:     Kalyana Krishna Varanasi
#
# Created:   04/01/2020
# Copyright:   (c) Hoder Solutions Pvt Ltd 2020 - Present
# Licence:   <your licence>
##########################################################################
from main import db


class JobTypes(db.Model):
    __tablename__ = "job_types"

    # unique identifier for a job type
    id = db.Column(db.Integer, primary_key=True)
    # name of the type of the job
    name = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return '{"id": {0}, "name": {1} }'.format(self.id, self.name)

    @classmethod
    def get_job_type(cls, _name):
        """
        currently we are getting the values hardcoded
        TODO: get the name->id values from database
        :param name:
        :return:
        """
        try:
            job_type = cls.query.filter_by(name=_name).first()
            if not job_type:
                return None
            else:
                return job_type.serialize()
        except:
            return None

    @classmethod
    def add_job_type(cls, _job_type):
        """
        currently we are getting the values hardcoded
        TODO: get the name->id values from database
        :param name: _job_type
        :return:
        """
        try:
            db.session.add(_job_type)
            db.session.commit()
            print(_job_type.name)
        except Exception as e:
            return {'msg': e}

        return _job_type

    @classmethod
    def get_all_job_types(cls):
        return [job_types.serialize() for job_types in cls.query.all()]

    def serialize(self):
        json_job_type = {
            "id": self.id,
            "name": self.name            
        }
        return json_job_type

    def serialize_without_users(self):
        json_job_type = {
            "id": self.id,
            "name": self.name
        }
        return json_job_type

