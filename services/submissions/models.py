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
    def get_application_from_id_user_id(cls, _id, _userid):
        application = cls.query.filter_by(requisitionid=_id, userid=_userid).first()
        return application
        
    
    @classmethod
    def get_requisitions_by_jobapplication_userid(classname, _userid):
        query = "select * from {} where id in (select requisitionid from job_applications where userid = {})".format(Requisitions.__tablename__,_userid)
        result = db.engine.execute(query)
        list_result =[]
        for requisition in result:
            requisition_object = dict(zip(result.keys(), requisition))
            list_result.append(Requisitions.serialize_dict(requisition_object))

        return list_result

    @classmethod
    def get_appliedusers_by_requisitionid(classname, _requisitionid):
        query = "select email from {} where id in ( select userid from job_applications where requisitionid = {})".format(Users.__tablename__,_requisitionid)
        result = db.engine.execute(query)
        list_result =[]
        for email in result:
            email_object = dict(zip(result.keys(), email))
            list_result.append(email_object)
        return list_result

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