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
from attributes.towns.models import Towns
from attributes.jobtypes.models import JobTypes
from attributes.qualifications.models import Qualifications
from attributes.states.models import States
from attributes.subjects.models import Subjects

class Requisitions(db.Model):
    __tablename__ =  "requisitions"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(2000), default="")
    jobtype = db.Column(db.Integer, db.ForeignKey('job_types.id'))
    gender = db.Column(db.Integer, default=0)
    subject = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    requisitiondetails = db.Column(db.String(2000), default="")
    responsibilities = db.Column(db.String(2000), default="")
    benefits = db.Column(db.String(2000), default="")
    eduexpdetails = db.Column(db.String(2000), default="")
    minexperience = db.Column(db.Integer, default=0)
    maxexperience = db.Column(db.Integer, default=0)
    telephone = db.Column(db.Integer, default=0)
    salary = db.Column(db.Integer, default=0)
    vacancy = db.Column(db.Integer, default=0)
    institution = db.Column(db.String(80), default="")
    submitter = db.Column(db.Integer, db.ForeignKey('users.id'))
    recruiter = db.Column(db.Integer, db.ForeignKey('users.id'))
    qualification = db.Column(db.Integer, db.ForeignKey('qualifications.id'))
    state = db.Column(db.Integer, db.ForeignKey('states.id'))
    district = db.Column(db.Integer, db.ForeignKey('districts.id'))
    town = db.Column(db.Integer, db.ForeignKey('towns.id'))
    registeredon = db.Column(db.DateTime, nullable=False, default=datetime.now())
    closedon = db.Column(db.DateTime)
    isactive = db.Column(db.Boolean, nullable=False, default=True)


    @classmethod
    def add_requisition(classname, _requisition):
        pass

    @classmethod
    def submit_requisition_from_json(classname, json_requisition):
        requisition = classname()
        if not json_requisition.get("title", None) is None:
            requisition.title = json_requisition.get("title", None)
        if not json_requisition.get("jobtype", None) is None:
            requisition.jobtype = json_requisition.get("jobtype", None)
        if not json_requisition.get("gender", None) is None:
            requisition.gender = json_requisition.get("gender", None)
        if not json_requisition.get("subject", None) is None:
            requisition.subject = json_requisition.get("subject", None)
        if not json_requisition.get("requisitiondetails", None) is None:
            requisition.requisitiondetails = json_requisition.get("requisitiondetails", None)
        if not json_requisition.get("responsibilities", None) is None:
            requisition.responsibilities = json_requisition.get("responsibilities", None)
        if not json_requisition.get("benefits", None) is None:
            requisition.benefits = json_requisition.get("benefits", None)
        if not json_requisition.get("eduexpdetails", None) is None:
            requisition.eduexpdetails = json_requisition.get("eduexpdetails", None)
        if not json_requisition.get("minexperience", None) is None:
            requisition.minexperience = json_requisition.get("minexperience", None)
        if not json_requisition.get("maxexperience", None) is None:
            requisition.maxexperience = json_requisition.get("maxexperience", None)
        if not json_requisition.get("telephone", None) is None:
            requisition.telephone = json_requisition.get("telephone", None)
        if not json_requisition.get("salary", None) is None:
            requisition.salary = json_requisition.get("salary", None)
        if not json_requisition.get("vacancy", None) is None:
            requisition.vacancy = json_requisition.get("vacancy", None)
        if not json_requisition.get("institution", None) is None:
            requisition.institution = json_requisition.get("institution", None)
        if not json_requisition.get("recruiter", None) is None:
            user = Users.get_user_by_username(json_requisition.get("recruiter", None))
            if not user is None:                
                requisition.recruiter = 1
        if not json_requisition.get("district", None) is None:
            requisition.district = json_requisition.get("district", None)
        if not json_requisition.get("submitter", None) is None:
            requisition.submitter = json_requisition.get("submitter", None)
        if not json_requisition.get("stateLocation", None) is None:
            requisition.state = json_requisition.get("stateLocation", None)
        if not json_requisition.get("town", None) is None:
            requisition.town = json_requisition.get("town", None)
        if not json_requisition.get("qualification", None) is None:
            requisition.qualification = json_requisition.get("qualification", None)
        if not json_requisition.get("deadline", None) is None:
            requisition.closedon = datetime.strptime(json_requisition.get("deadline", None), "%Y-%m-%dT%H:%M:%S.%fZ")
        db.session.add(requisition)
        db.session.commit()
        return requisition

    @classmethod
    def get_requisitions_by_filter(classname, filter):
        query = "select * from requisitions where "
        for key, value in filter.items():
            query = "{} {} = {}".format(query, key, value)
        result = db.engine.execute(query)
        list_result =[]
        for requisition in result:
            requisition_object = dict(zip(result.keys(), requisition))
            list_result.append(Requisitions.serialize_dict(requisition_object))

        return list_result

    def serialize(self):
        json_requisition = {
            "id": self.id,
            "title": self.title,
            "subject": Subjects.get_subject_from_id(self.subject).subject,
            #"Recruiter": users.Users.get_user_by(self.recruiter).email,
            #"Minimum Qualification Needed": Qualifications.get_qualification_from_id(self.qualification).qualification,
            "district": Districts.get_district_from_id(self.district).district,
            "state": States.get_state_from_id(self.state).state,
			"town": Towns.get_town_from_id(self.town).town,
            "institution": self.institution,
            "minexperience": self.minexperience,
            "maxexperience": self.maxexperience,
            "requisitiondetails": self.requisitiondetails,
            "responsibilities": self.responsibilities,
            "benefits": self.benefits,
            "eduexpdetails": self.eduexpdetails,
            "salary": self.salary,
            "vacancy": self.vacancy,
            "gender": self.gender,
            "jobtype": self.jobtype,
            "submitter": self.submitter,
            "registeredon":self.registeredon.strftime("%d-%B-%Y"),
            "closedon":self.closedon.strftime("%d-%B-%Y")
        }
        return json_requisition

    @classmethod
    def serialize_dict(classname, requisition_dict):
        json_requisition = {
            "id": requisition_dict['id'],
            "title": requisition_dict['title'],
            "subject": Subjects.get_subject_from_id(requisition_dict['subject']).subject,
            #"Recruiter": users.Users.get_user_by(self.recruiter).email,
            #"Minimum Qualification Needed": Qualifications.get_qualification_from_id(requisition_dict['qualification']).qualification,
            "district": Districts.get_district_from_id(requisition_dict['district']).district,
            "state": States.get_state_from_id(requisition_dict['state']).state,
			"town": Towns.get_town_from_id(requisition_dict['town']).town,
            "institution": requisition_dict['institution'],
            "minexperience": requisition_dict['minexperience'],
            "maxexperience": requisition_dict['maxexperience'],
            "requisitiondetails": requisition_dict['requisitiondetails'],
            "responsibilities": requisition_dict['responsibilities'],
            "benefits": requisition_dict['benefits'],
            "eduexpdetails": requisition_dict['eduexpdetails'],
            "salary": requisition_dict['salary'],
            "vacancy": requisition_dict['vacancy'],
            "gender": requisition_dict['gender'],
            "jobtype": requisition_dict['jobtype'],
            "submitter": requisition_dict['submitter'],
            "registeredon":requisition_dict['registeredon'],
            "closedon":requisition_dict['deadline']
        }
        return json_requisition