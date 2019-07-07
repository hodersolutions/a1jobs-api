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


class Institutions(db.Model):
    __tablename__ =  "institutions"
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.Integer)
    institution = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "institution":{1}}'.format(self.id, self.institution)

    @classmethod
    def get_all_institutions(cls):
        institutions = Institutions.query.all()
        institutions_json = [institution.serialize() for institution in institutions]
        return institutions_json

    @classmethod
    def get_institution_from_id(cls, id):
        institution = cls.query.get(id)
        return institution

    @classmethod
    def delete_institution_from_id(cls, id):
        institution = cls.get_institution_from_id(id)
        if institution is None:
            return None
        db.session.delete(institution)
        db.session.commit()
        return institution

    @classmethod
    def submit_institution_from_json(cls, json_institution):
        institution = cls(institution=json_institution['institution'], district=json_institution["district"])
        db.session.add(institution)
        db.session.commit()
        return institution

    # todo:json encoding needed
    def serialize(self):
        json_institution = {
            'id' : self.id ,
            'institution' : self.institution,
        }
        return json_institution
