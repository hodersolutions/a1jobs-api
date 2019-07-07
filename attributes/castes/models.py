##########################################################################
# Name:     Caste Decorators
# Purpose: File contains decorators for caste validations and Authentications
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db


class Castes(db.Model):
    __tablename__ = "castes"
    id = db.Column(db.Integer, primary_key=True)
    caste = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "caste":{1}}'.format(self.id, self.caste)

    @classmethod
    def get_all_castes(cls):
        castes = Castes.query.all()
        castes_json = [caste.serialize() for caste in castes]
        return castes_json

    @classmethod
    def get_caste_from_id(cls, id):
        caste = cls.query.get(id)
        return caste

    @classmethod
    def delete_caste_from_id(cls, id):
        caste = cls.get_caste_from_id(id)
        if caste is None:
            return None
        db.session.delete(caste)
        db.session.commit()
        return caste

    @classmethod
    def submit_caste_from_json(cls, json_caste):
        caste = cls(caste=json_caste['caste'])
        db.session.add(caste)
        db.session.commit()
        return caste

    # todo:json encoding needed
    def serialize(self):
        json_caste = {
            'id': self.id,
            'caste': self.caste,
        }
        return json_caste
