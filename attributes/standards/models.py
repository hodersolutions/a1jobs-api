##########################################################################
# Name:     Standard Decorators
# Purpose: File contains decorators for standard validations and Authentications
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db


class Standards(db.Model):
    __tablename__ = "standards"
    id = db.Column(db.Integer, primary_key=True)
    standard = db.Column(db.String(200), nullable=False)
    section_list = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '{"id":{0}, "standard":{1}}'.format(self.id, self.standard)

    @classmethod
    def get_all_standards(cls):
        standards = Standards.query.all()
        standards_json = [standard.serialize() for standard in standards]
        return standards_json

    @classmethod
    def get_standard_from_id(cls, id):
        standard = cls.query.get(id)
        return standard

    @classmethod
    def delete_standard_from_id(cls, id):
        standard = cls.get_standard_from_id(id)
        if standard is None:
            return None
        db.session.delete(standard)
        db.session.commit()
        return standard

    @classmethod
    def submit_standard_from_json(cls, json_standard):
        standard = cls(standard=json_standard['standard'])
        db.session.add(standard)
        db.session.commit()
        return standard

    # todo:json encoding needed
    def serialize(self):
        json_standard = {
            'id': self.id,
            'standard': self.standard,
            'section_list': self.section_list
        }
        return json_standard
