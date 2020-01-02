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
from logins.models import Users
from attributes.districts.models import Districts
from attributes.qualifications.models import Qualifications
from attributes.states.models import States
from attributes.subjects.models import Subjects

class Requisitions(db.Model):
    __tablename__ =  "requisitions"
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    requisitiondetails = db.Column(db.String(2000), default="")
    minexperience = db.Column(db.Integer, default=0)
    maxexperience = db.Column(db.Integer, default=0)
    telephone = db.Column(db.Integer, default=0)
    institution = db.Column(db.String(80), default="")
    description = db.Column(db.String(80), default="")
    recruiter = db.Column(db.Integer, db.ForeignKey('users.id'))
    qualification = db.Column(db.Integer, db.ForeignKey('qualifications.id'))
    state = db.Column(db.Integer, db.ForeignKey('states.id'))
    district = db.Column(db.Integer, db.ForeignKey('districts.id'))
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.now())
    closed_on = db.Column(db.DateTime)
    isactive = db.Column(db.Boolean, nullable=False, default=True)


    @classmethod
    def add_requisition(classname, _requisition):
        pass

    @classmethod
    def submit_requisition_from_json(classname, json_requisition):
        requisition = classname()
        if not json_requisition.get("subject", None) is None:
            requisition.subject = json_requisition.get("subject", None)
        if not json_requisition.get("requisitiondetails", None) is None:
            requisition.requisitiondetails = json_requisition.get("requisitiondetails", None)
        if not json_requisition.get("minexperience", None) is None:
            requisition.minexperience = json_requisition.get("minexperience", None)
        if not json_requisition.get("maxexperience", None) is None:
            requisition.maxexperience = json_requisition.get("maxexperience", None)
        if not json_requisition.get("telephone", None) is None:
            requisition.telephone = json_requisition.get("telephone", None)
        if not json_requisition.get("institution", None) is None:
            requisition.institution = json_requisition.get("institution", None)
        if not json_requisition.get("submitter", None) is None:
            user = Users.get_user_by_username(json_requisition.get("submitter", None))
            if not user is None:
                print(user)
                requisition.recruiter = 1
        if not json_requisition.get("district", None) is None:
            requisition.district = json_requisition.get("district", None)
        if not json_requisition.get("state", None) is None:
            requisition.state = json_requisition.get("state", None)
        if not json_requisition.get("qualification", None) is None:
            requisition.qualification = json_requisition.get("qualification", None)
        if not json_requisition.get("description", None) is None:
            requisition.description = json_requisition.get("description", None)
        db.session.add(requisition)
        db.session.commit()
        return requisition

    @classmethod
    def get_requisitions_by_filter(classname, filter):
        query = "select * from requisitions where "
        for key, value in filter.items():
            query = "{} {} = {}".format(query, key, value)
        print(query)
        result = db.engine.execute(query)
        list_result =[]
        for requisition in result:
            requisition_object = dict(zip(result.keys(), requisition))
            list_result.append(Requisitions.serialize_dict(requisition_object))

        return list_result

    def serialize(self):
        json_requisition = {
            "Id": self.id,
            "Title": self.description,
            "Subject": Subjects.get_subject_from_id(self.subject).subject,
            #"Recruiter": users.Users.get_user_by(self.recruiter).email,
            # "Minimum Qualification Needed": Qualifications.get_qualification_from_id(self.qualification).qualification,
            "District": Districts.get_district_from_id(self.district).district,
            "State": States.get_state_from_id(self.state).state,
            "Institution": self.institution,
            "Minimum years of Experience": self.minexperience,
            "Requisition Description": self.requisitiondetails,
            "Opened on":self.registered_on.strftime("%d-%B")
        }
        return json_requisition

    @classmethod
    def serialize_dict(classname, requisition_dict):
        json_requisition = {
            "Id": requisition_dict['id'],
            "Title": requisition_dict['description'],
            #"Recruiter": users.Users.get_user_by(self.recruiter).email,
            "Minimum Qualification Needed": Qualifications.get_qualification_from_id(requisition_dict['qualification']).qualification,
            "District": Districts.get_district_from_id(requisition_dict['district']).district,
            "State": States.get_state_from_id(requisition_dict['state']).state,
            "School": requisition_dict['institution'],
            "Minimum years of Experience": requisition_dict['minexperience'],
            "Requisition Description": requisition_dict['requisitiondetails'],
            "Opened on":requisition_dict['registered_on']
        }
        return json_requisition