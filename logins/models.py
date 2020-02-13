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
from passlib.hash import pbkdf2_sha256 as sha256
from attributes.qualifications.models import Qualifications
from attributes.states.models import States
from attributes.subjects.models import Subjects
from attributes.districts.models import Districts
from attributes.towns.models import Towns


class Users(db.Model):
    __tablename__ = "users"

    # unique identifier for a user
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # encrypted value
    password = db.Column(db.String(200), nullable=False)
    # email of the user, cannot be null, and should be unique
    email = db.Column(db.String(80), nullable=True)
    # mobile number of the user
    mobile = db.Column(db.String(20), nullable=True)
    # registration time
    creation_date = db.Column(db.DateTime, nullable=True, default=datetime.now())
    # If user is not with the Org anymore, TODO: use this effectively
    is_active = db.Column(db.Boolean, nullable=True, default=True)
    # Is the user a recruiter
    is_recruiter = db.Column(db.Boolean, nullable=True)
    # Basic profiles
    profiles = db.relationship('UsersProfileBasic', backref='enquiry', lazy=True)

    # foreign key from the user_details table
    # roles = db.relationship('UserDetails', backref='enquiry', lazy=True)

    def __repr__(self):
        return "{ email: {1}, id: {2}, mobile: {3} }".format(self.email, self.id, self.mobile)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    def fullname(self):
        return "{} {}".format(self.first_name, self.last_name)

    @classmethod
    def add_user(cls, json_user):        
        try:
            _new_user = cls()

            if not json_user.get("email", None) is None:
                _new_user.email = json_user.get("email", None)
            if not json_user.get("mobile", None) is None:
                _new_user.mobile = json_user.get("mobile", None)
            if not json_user.get("password", None) is None:
                _new_user.password = cls.generate_hash(json_user.get("password", None))
            if not json_user.get("is_recruiter", None) is None:
                _new_user.is_recruiter = json_user.get("is_recruiter", None)
                
            db.session.add(_new_user)
            # add the role to the user before the db commit
            # user_roles.UserRoles.add_user_role(_new_user.id, _role)
            db.session.commit()
        except Exception as e:
            return None, e

        return _new_user.serialize(), None

    @classmethod
    def get_all_users(cls):
        return [user.serialize() for user in cls.query.all()]

    @classmethod
    def get_user_by_email(cls, _email):
        try:
            user_object = cls.query.filter_by(email=_email).first()
            if not user_object:
                return user_object
            else:
                return user_object.serialize()
        except:
            return None

    @classmethod
    def get_user_by_mobile(cls, _mobile):
        try:
            user_object = cls.query.filter_by(mobile=_mobile).first()
            if not user_object:
                return user_object
            else:
                return user_object.serialize()
        except:
            return None

    @classmethod
    def get_users_from_text(cls, text):
        query = """select id, Users.firstname, Users.lastname from Users where Users.firstname like "%{}%"
        or Users.lastname like "%{}%" or Users.username like "%{}%" """.format(text, text, text)
        result = db.engine.execute(query)
        list_result = []
        for user in result:
            user_dict = {}
            user_dict['id'] = user[0]
            user_dict['label'] = "{} {}".format(user[1], user[2])
            list_result.append(user_dict)
        return list_result

    @classmethod
    def get_user_by_id(cls, id):
        user_object = cls.query.get(id)
        if not user_object:
            return None
        else:
            return user_object

    @classmethod
    def delete_user_by_uid(cls, _uid):
        try:
            cls.query.filter_by(uid=_uid).delete() # todo: use is_active instead of deleting the record
            db.session.commit()
        except:
            return False

        return True

    @classmethod
    def update_user_by_email(cls, _email, _user):
        try:
            user_to_update = cls.query.filter_by(email=_email).first()
            user_to_update.email = _user.email
            db.session.commit()
        except:
            return False

        return cls.get_user_by_email(_user.email)

    @classmethod
    def update_user_by_mobile(cls, _mobile, _user):
        try:
            user_to_update = cls.query.filter_by(mobile=_mobile).first()
            user_to_update.mobile = _user.mobile
            db.session.commit()
        except:
            return False

        return cls.get_user_by_mobile(_user.mobile)
        
    def serialize(self):
        json_user = {
            "id": self.id,
            "mobile": self.mobile,
            "email": self.email,
            "is_recruiter": self.is_recruiter
        }
        return json_user

    def serialize_without_roles(self):
        json_user = {
            "id": self.id,
            "mobile": self.mobile,
            "email": self.email,
            "is_recruiter": self.is_recruiter
        }
        return json_user

    ############################################################################################
    # All the functions to retrieve seeker details and update them
    ############################################################################################
    def update_user(self):
        db.session.add(self)
        db.session.commit()
        return True, False


class UsersProfileBasic(db.Model):
    __tablename__ = "users_profile_basic"

    # unique identifier for a user
    id = db.Column(db.Integer, primary_key=True)
    # Foreign key user id
    userid = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    # Firstname
    firstname = db.Column(db.String(30), nullable=True)
    # Middlename
    middlename = db.Column(db.String(30), nullable=True)
    # Lastname
    lastname = db.Column(db.String(30), nullable=True)
    # Fathername
    fathername = db.Column(db.String(90), nullable=True)
    #DOB
    dob = db.Column(db.DateTime, default=datetime.now())
    #address
    address = db.Column(db.String(2000), nullable=True)
    #pan number
    pan = db.Column(db.String(80), nullable=True)
    # Gender
    gender = db.Column(db.Integer, default=0)
    # Nationality
    nationality = db.Column(db.String(20), nullable=True)
    #current designation
    designation = db.Column(db.String(200), nullable=True)
    # CTC
    ctc = db.Column(db.Integer, default=None)
    # ECTC
    ectc = db.Column(db.Integer, default=None)
    #years of experience
    totalexperience = db.Column(db.Integer, default=None)
    #teaching subject
    teachingsubject = db.Column(db.Integer,db.ForeignKey('subjects.id'))
    #circulum
    circulum = db.Column(db.Integer, default=0)
    #currentorganization
    currentorganization = db.Column(db.String(80), default="")
    #department
    department = db.Column(db.Integer, default=0)
    #qualification
    qualification = db.Column(db.Integer, db.ForeignKey('qualifications.id'))
    #state
    state = db.Column(db.Integer, db.ForeignKey('states.id'))
    #district
    district = db.Column(db.Integer, db.ForeignKey('districts.id'))
    #town
    town = db.Column(db.Integer, db.ForeignKey('towns.id'))
    #teaching medium
    teachingmedium = db.Column(db.Integer, default=0)
    #segment
    segment = db.Column(db.Integer, default=0)
    # registration date & time
    creation_date = db.Column(db.DateTime, nullable=True, default=datetime.now())
    # updated date & time
    updation_date = db.Column(db.DateTime, nullable=True, default=datetime.now())
    
    def __repr__(self):
        return "{ fullname: {1}, id: {2} }".format(self.firstname + self.middlename + self.lastname, self.id)

    def fullname(self):
        return "{} {} {}".format(self.firstname, self.middlename, self.lastname)

    @classmethod
    def submit_profile_from_json(cls, json_profile):        
        profile = cls()                
        try:
            if not json_profile.get("userid", None) is None:                
                profile.userid = int(json_profile.get("userid", None))

            if not json_profile.get("firstname", None) is None:
                profile.firstname = json_profile.get("firstname", None)

            if not json_profile.get("lastname", None) is None:
                profile.lastname = json_profile.get("lastname", None)

            if not json_profile.get("middlename", None) is None:
                profile.middlename = json_profile.get("middlename", None)

            if not json_profile.get("fathername", None) is None:
                profile.fathername = json_profile.get("fathername", None)

            if not json_profile.get("gender", None) is None:
                profile.gender = json_profile.get("gender", None)

            if not json_profile.get("nationality", None) is None:
                profile.nationality = json_profile.get("nationality", None)

            if not json_profile.get("ctc", None) is None:                        
                if json_profile.get("ctc") == '':
                    profile.ctc = None
                else:
                    profile.ctc = int(json_profile.get("ctc", None))

            if not json_profile.get("ectc", None) is None:
                if json_profile.get("ectc") == '':
                    profile.ectc = None
                else:
                    profile.ectc = int(json_profile.get("ectc", None))

            if not json_profile.get("totalexperience", None) is None:                        
                if json_profile.get("totalexperience") == '':
                    profile.totalexperience = None
                else:
                    profile.totalexperience = int(json_profile.get("totalexperience", None))

            if not json_profile.get("teachingsubject", None) is None:
                profile.teachingsubject = json_profile.get("teachingsubject", None)

            if not json_profile.get("circulum", None) is None:
                profile.circulum = json_profile.get("circulum", None)

            if not json_profile.get("currentorganization", None) is None:
                profile.currentorganization = json_profile.get("currentorganization", None)

            if not json_profile.get("department", None) is None:
                profile.department = json_profile.get("department", None)

            if not json_profile.get("qualification", None) is None:
                profile.qualification = json_profile.get("qualification", None)

            if not json_profile.get("stateLocation", None) is None:
                profile.state = json_profile.get("stateLocation", None)

            if not json_profile.get("district", None) is None:
                profile.district = json_profile.get("district", None)

            if not json_profile.get("town", None) is None:
                profile.town = json_profile.get("town", None)

            if not json_profile.get("teachingmedium", None) is None:
                profile.teachingmedium = json_profile.get("teachingmedium", None)

            if not json_profile.get("segment", None) is None:
                profile.segment = json_profile.get("segment", None)

            if not json_profile.get("dob", None) is None:
                profile.dob = datetime.strptime(json_profile.get("dob", None), "%d/%m/%Y")

            if not json_profile.get("address", None) is None:
                profile.address = json_profile.get("address", None)

            if not json_profile.get("designation", None) is None:
                profile.designation = json_profile.get("designation", None)

            if not json_profile.get("pan", None) is None:
                profile.pan = json_profile.get("pan", None)

            db.session.add(profile)
            db.session.commit()
        except Exception as e:
            return None, e

        return cls.get_user_profile_by_userid(profile.userid), None

    @classmethod
    def get_all_user_profiles(cls, filter):
        if filter:
            return cls.query.filter_by('{} = {}'.format((key,value) for key,value in filter.items())).first()
        query = "select  up.*,u.email,u.mobile from users_profile_basic up inner join users u on up.userid = u.id and u.is_recruiter = False"
        result = db.engine.execute(query)
        list_result = []
        if not result:
            return None
        for userprofile in result:
            userprofile_dict = dict(zip(result.keys(), userprofile))
            list_result.append(UsersProfileBasic.serialize_view_userprofile(userprofile_dict))
        return  list_result
        
    @classmethod
    def get_user_profile_by_userid(cls, _userid):
        try:
            if not _userid is None:
                profile = cls.query.filter_by(userid=_userid).first()
            return profile, None

        except Exception as e:
            return None, e
            

    @classmethod
    def get_profile_joining_user_via_userid(cls, _userid):
        try:
            query = "select  up.*,u.email,u.mobile from users_profile_basic up inner join users u on up.userid = u.id where up.userid = {}".format(_userid)       
            result = db.engine.execute(query)
            if not result:
                return None
            for userprofile in result:
                userprofile_dict = dict(zip(result.keys(), userprofile))                
            return  UsersProfileBasic.serialize_view_userprofile(userprofile_dict)        
        except:
            return None

    @classmethod
    def get_users_from_text(cls, text):
        query = """select id, UsersProfileBasic.firstname, UsersProfileBasic.lastname from UsersProfileBasic where UsersProfileBasic.firstname like "%{}%"
        or UsersProfileBasic.lastname like "%{}%" or UsersProfileBasic.middlename like "%{}%" """.format(text, text, text)
        result = db.engine.execute(query)
        list_result = []
        for user in result:
            user_dict = {}
            user_dict['id'] = user[0]
            user_dict['label'] = "{} {}".format(user[1], user[2])
            list_result.append(user_dict)
        return list_result

    @classmethod
    def get_userprofile_by_id(cls, id):
        user_object = cls.query.get(id)
        if not user_object:
            return None
        else:
            return user_object

    @classmethod
    def get_userprofile_joining_user(cls, id):
        query = "select  up.*,u.email,u.mobile from users_profile_basic up inner join users u on up.userid = u.id where up.id = {}".format(id)
        result = db.engine.execute(query)
        if not result:
            return None
        for userprofile in result:
            userprofile_dict = dict(zip(result.keys(), userprofile))
        return  UsersProfileBasic.serialize_view_userprofile(userprofile_dict)

    @classmethod
    def get_profile_joining_user_via(cls, id):
        query = "select  up.*,u.email,u.mobile from users_profile_basic up inner join users u on up.userid = u.id where up.id = {}".format(id)
        result = db.engine.execute(query)
        if not result:
            return None
        for userprofile in result:
            userprofile_dict = dict(zip(result.keys(), userprofile))
        return  UsersProfileBasic.serialize_view_userprofile(userprofile_dict)

    @classmethod
    def delete_user_by_uid(cls, _id):
        try:
            cls.query.filter_by(id=_id).delete()
            db.session.commit()
        except:
            return False

        return True

    @classmethod
    def add_or_update_user_by_userid(cls, json_profile):
        try: 
            if not json_profile.get("userid", None) is None:
                profile = cls.query.filter_by(userid=int(json_profile.get("userid"))).first()
                error = None
                if profile is None:
                    profile, error = cls.submit_profile_from_json(json_profile)
                else:
                    if not json_profile.get("firstname", None) is None:
                        profile.firstname = json_profile.get("firstname", None)

                    if not json_profile.get("lastname", None) is None:
                        profile.lastname = json_profile.get("lastname", None)

                    if not json_profile.get("middlename", None) is None:
                        profile.middlename = json_profile.get("middlename", None)

                    if not json_profile.get("fathername", None) is None:
                        profile.fathername = json_profile.get("fathername", None)

                    if not json_profile.get("gender", None) is None:
                        profile.gender = json_profile.get("gender", None)

                    if not json_profile.get("nationality", None) is None:
                        profile.nationality = json_profile.get("nationality", None)

                    if not json_profile.get("ctc", None) is None:                        
                        if json_profile.get("ctc") == '':
                            profile.ctc = None
                        else:
                            profile.ctc = int(json_profile.get("ctc", None))

                    if not json_profile.get("ectc", None) is None:
                        if json_profile.get("ectc") == '':
                            profile.ectc = None
                        else:
                            profile.ectc = int(json_profile.get("ectc", None))

                    if not json_profile.get("totalexperience", None) is None:                        
                        if json_profile.get("totalexperience") == '':
                            profile.totalexperience = None
                        else:
                            profile.totalexperience = int(json_profile.get("totalexperience", None))

                    if not json_profile.get("teachingsubject", None) is None:
                        profile.teachingsubject = json_profile.get("teachingsubject", None)

                    if not json_profile.get("circulum", None) is None:
                        profile.circulum = json_profile.get("circulum", None)

                    if not json_profile.get("currentorganization", None) is None:
                        profile.currentorganization = json_profile.get("currentorganization", None)

                    if not json_profile.get("department", None) is None:
                        profile.department = json_profile.get("department", None)

                    if not json_profile.get("qualification", None) is None:
                        profile.qualification = json_profile.get("qualification", None)

                    if not json_profile.get("stateLocation", None) is None:
                        profile.state = json_profile.get("stateLocation", None)

                    if not json_profile.get("district", None) is None:
                        profile.district = json_profile.get("district", None)

                    if not json_profile.get("town", None) is None:
                        profile.town = json_profile.get("town", None)

                    if not json_profile.get("teachingmedium", None) is None:
                        profile.teachingmedium = json_profile.get("teachingmedium", None)

                    if not json_profile.get("segment", None) is None:
                        profile.segment = json_profile.get("segment", None)

                    if not json_profile.get("dob", None) is None:
                        profile.dob = datetime.strptime(json_profile.get("dob",None),"%d/%m/%Y")

                    if not json_profile.get("address", None) is None:
                        profile.address = json_profile.get("address", None)

                    if not json_profile.get("designation", None) is None:
                        profile.designation = json_profile.get("designation", None)
                        
                    if not json_profile.get("pan", None) is None:
                        profile.pan = json_profile.get("pan", None)

                    db.session.add(profile)
                    db.session.commit()
                return profile, error
            else:
                return None, None

        except Exception as e:            
            return None, e
    
    def serialize(self):
        json_user = {
            "id": self.id,
            "userid": self.userid,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "fullname": self.fullname(),
            "fathername": self.fathername,
            "gender": self.gender,
            "nationality": self.nationality,
            "dob": self.dob.strftime("%d/%m/%Y"),
            "address": self.address,
            "pan" : self.pan,
            "designation":self.designation,
            "ctc": self.ctc,
            "ectc": self.ectc,
            "teachingsubject": self.teachingsubject,
            "district": self.district,
            "stateLocation": self.state,
			"town": self.town,
            "qualification": self.qualification,
            "totalexperience": self.totalexperience,
            "circulum": self.circulum,
            "teachingmedium": self.teachingmedium,
            "currentorganization": self.currentorganization,
            "segment": self.segment,
            "department": self.department
        }        
        return json_user

    def serialize_without_roles(self):
        json_user = {
            "id": self.id,
            "userid": self.userid,
            "firstname": self.firstname,
            "middlename": self.middlename,
            "lastname": self.lastname,
            "fullname": self.fullname(),
            "fathername": self.fathername,
            "gender": self.gender,
            "nationality": self.nationality,
            "dob": self.dob.strftime("%d/%m/%Y"),
            "address": self.address,
            "pan" : self.pan,
            "designation":self.designation,
            "ctc": self.ctc,
            "ectc": self.ectc,
            "teachingsubject": Subjects.get_subject_from_id(self.teachingsubject).subject,
            "district": Districts.get_district_from_id(self.district).district,
            "stateLocation": States.get_state_from_id(self.state).state,
			"town": Towns.get_town_from_id(self.town).town,
            "qualification": Qualifications.get_qualification_from_id(self.qualification).qualification,
            "totalexperience": self.totalexperience,
            "circulum": self.circulum,
            "teachingmedium": self.teachingmedium,
            "currentorganization": self.currentorganization,
            "segment": self.segment,
            "department": self.department
        }
        return json_user

    @classmethod
    def serialize_view_userprofile(cls,userprofile_dict):
        teachingsubject = "N/A" if userprofile_dict["teachingsubject"] == 0 else Subjects.get_subject_from_id(userprofile_dict["teachingsubject"]).subject
        district = "N/A" if userprofile_dict["district"] == 0 else Districts.get_district_from_id(userprofile_dict["district"]).district
        stateLocation = "N/A" if userprofile_dict["state"] == 0 else States.get_state_from_id(userprofile_dict["state"]).state
        town = "N/A" if userprofile_dict["town"]==0 else Towns.get_town_from_id(userprofile_dict["town"]).town
        qualification = "N/A" if userprofile_dict["qualification"] else Qualifications.get_qualification_from_id(userprofile_dict["qualification"]).qualification

        json_user = {
            "id": userprofile_dict["id"],
            "userid": userprofile_dict["userid"],
            "firstname": userprofile_dict["firstname"],
            "middlename": userprofile_dict["middlename"],
            "lastname": userprofile_dict["lastname"],
            "fullname": userprofile_dict["firstname"] +' ' + userprofile_dict["middlename"] + ' ' + userprofile_dict["lastname"],
            "fathername": userprofile_dict["fathername"],
            "gender": userprofile_dict["gender"],
            "nationality": userprofile_dict["nationality"],
            "dob": userprofile_dict["dob"].strftime("%d/%m/%Y"),
            "address": userprofile_dict["address"],
            "pan" : userprofile_dict["pan"],
            "designation":userprofile_dict["designation"],
            "ctc": userprofile_dict["ctc"],
            "ectc": userprofile_dict["ectc"],
            "teachingsubject": teachingsubject,
            "district": district,
            "stateLocation": stateLocation,
			"town": town,
            "qualification": qualification,
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

        

class UsersAudit(db.Model):
    __tablename__ = "users_audit"

    # unique identifier for a user
    audit_id = db.Column(db.Integer, primary_key=True)
    # user identifier
    id = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(200), nullable=True)
    # first name of a user
    first_name = db.Column(db.String(80), nullable=True)
    # last name of a user
    last_name = db.Column(db.String(80), nullable=True)
    # email of the user, cannot be null, and should be unique
    email = db.Column(db.String(80), nullable=True)
    # mobile number of the user
    mobile = db.Column(db.String(80), nullable=True)
    # registration time
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    # If user is not with the Org anymore, TODO: use this effectively
    is_active = db.Column(db.Boolean, nullable=True, default=1)
    # user who is enrolling this record
    user_creator = db.Column(db.Integer, nullable=True)
    # user who is updating this record
    user_modifier = db.Column(db.Integer, nullable=True)
    # json value to store user specific details
    details = db.Column(db.String(2000), nullable=True)
