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
from attributes.qualifications.models import Qualifications
from attributes.states.models import States
from attributes.subjects.models import Subjects
from attributes.districts.models import Districts
from attributes.towns.models import Towns

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
        query = "select  up.*, u.email, u.mobile from users_profile_basic up inner join users u on up.userid = u.id where u.id in (select userid from job_applications where requisitionid = {})".format(_requisitionid)
        result = db.engine.execute(query)
        list_result =[]
        for profile in result:
            profile_object = dict(zip(result.keys(), profile))
            list_result.append(JobApplications.serialize_view_userprofile(profile_object))
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

    @classmethod
    def serialize_view_userprofile(cls,userprofile_dict):
        json_user = {
            "id": userprofile_dict["id"],
            "userid": userprofile_dict["userid"],
            "firstname": userprofile_dict["firstname"],
            "middlename": userprofile_dict["middlename"],
            "lastname": userprofile_dict["lastname"],
            "fullname": userprofile_dict["firstname"] +' '+ userprofile_dict["middlename"] +' ' +userprofile_dict["lastname"],
            "fathername": userprofile_dict["fathername"],
            "gender": userprofile_dict["gender"],
            "nationality": userprofile_dict["nationality"],
            "dob": datetime.strptime(userprofile_dict["dob"],'%Y-%m-%d %H:%M:%S.%f').strftime("%d-%B-%Y"),
            "address": userprofile_dict["address"],
            "pan" : userprofile_dict["pan"],
            "designation":userprofile_dict["designation"],
            "ctc": userprofile_dict["ctc"],
            "ectc": userprofile_dict["ectc"],
            "teachingsubject": Subjects.get_subject_from_id(userprofile_dict["teachingsubject"]).subject,
            "district": Districts.get_district_from_id(userprofile_dict["district"]).district,
            "stateLocation": States.get_state_from_id(userprofile_dict["state"]).state,
			"town": Towns.get_town_from_id(userprofile_dict["town"]).town,
            "qualification": Qualifications.get_qualification_from_id(userprofile_dict["qualification"]).qualification,
            "totalexperience": userprofile_dict["totalexperience"],
            "circulum": userprofile_dict["circulum"],
            "teachingmedium": userprofile_dict["teachingmedium"],
            "currentorganization": userprofile_dict["currentorganization"],
            "segment": userprofile_dict["segment"],
            "department": userprofile_dict["department"],
            "email": userprofile_dict["email"],
            "mobile":userprofile_dict["mobile"]
        }        
        return json_user