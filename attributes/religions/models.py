##########################################################################
# Name:     Religion Decorators
# Purpose: File contains decorators for religion validations and Authentications
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db


class Religions(db.Model):
    __tablename__ = "religions"
    id = db.Column(db.Integer, primary_key=True)
    religion = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "religion":{1}}'.format(self.id, self.religion)

    @classmethod
    def get_all_religions(cls):
        religions = Religions.query.all()
        religions_json = [religion.serialize() for religion in religions]
        return religions_json

    @classmethod
    def get_religion_from_id(cls, id):
        religion = cls.query.get(id)
        return religion

    @classmethod
    def delete_religion_from_id(cls, id):
        religion = cls.get_religion_from_id(id)
        if religion is None:
            return None
        db.session.delete(religion)
        db.session.commit()
        return religion

    @classmethod
    def submit_religion_from_json(cls, json_religion):
        religion = cls(religion=json_religion['religion'])
        db.session.add(religion)
        db.session.commit()
        return religion

    # todo:json encoding needed
    def serialize(self):
        json_religion = {
            'id': self.id,
            'religion': self.religion,
        }
        return json_religion
