##########################################################################
# Name:     job_applications
# Purpose: File contains districs
#
# Author:     Kalyana Krishna Varanasi
#
# Created:   05/01/2020
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db
from datetime import datetime
from logins.models import Users
from services.requisitions.models import Requisitions

class JobApplications(db.Model):
    __tablename__ =  "job_applications"

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey('users.id'))
    requisitionid = db.Column(db.Integer, db.ForeignKey('requisitions.id'))
    # Submission time
    submission_date = db.Column(db.DateTime, nullable=True, default=datetime.now())
    
    def __repr__(self):
        return '{"id":{0}, "userid":{1}, "requisitionid":{2}}'.format(self.id, self.userid, self.requisitionid)

    @classmethod
    def get_all_applications(cls):
        applications = JobApplications.query.all()
        applications_json = [application.serialize() for application in applications]
        return applications_json

    @classmethod
    def get_application_from_id(cls, id):
        application = cls.query.get(id)
        return application

    @classmethod
    def delete_application_from_id(cls, id):
        application = cls.get_application_from_id(id)
        if application is None:
            return None
        db.session.delete(application)
        db.session.commit()
        return application

    @classmethod
    def submit_application_from_json(cls, json_application):
        application = cls(userid=json_application['userid'], requisitionid=json_application['requisitionid'])
        db.session.add(application)
        db.session.commit()
        return application

    def serialize(self):
        json_application = {
            'id': self.id,
            'userid': self.userid,
            'requisitionid': self.requisitionid,
            'submission_date': self.submission_date
        }
        return json_application