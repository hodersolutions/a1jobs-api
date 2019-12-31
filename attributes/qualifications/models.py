##########################################################################
# Name:     Qualification Decorators
# Purpose: File contains decorators for qualification validations and Authentications
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db


class Qualifications(db.Model):
    __tablename__ = "qualifications"
    id = db.Column(db.Integer, primary_key=True)
    qualification = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "qualification":{1}}'.format(self.id, self.qualification)

    @classmethod
    def get_all_qualifications(cls):
        qualifications = Qualifications.query.all()
        qualifications_json = [qualification.serialize() for qualification in qualifications]
        return qualifications_json

    @classmethod
    def get_qualification_from_id(cls, id):
        qualification = cls.query.get(id)
        return qualification

    @classmethod
    def delete_qualification_from_id(cls, id):
        qualification = cls.get_qualification_from_id(id)
        if qualification is None:
            return None
        db.session.delete(qualification)
        db.session.commit()
        return qualification

    @classmethod
    def submit_qualification_from_json(cls, json_qualification):
        qualification = cls(qualification=json_qualification['qualification'])
        db.session.add(qualification)
        db.session.commit()
        return qualification

    # todo:json encoding needed
    def serialize(self):
        json_qualification = {
            'id': self.id,
            'qualification': self.qualification,
        }
        return json_qualification
