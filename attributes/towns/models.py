##########################################################################
# Name:     Town Decorators
# Purpose: File contains decorators for town validations and Authentications
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db


class Towns(db.Model):
    __tablename__="towns"
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.Integer)
    town = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "town":{1}}'.format(self.id, self.town)

    @classmethod
    def get_all_towns(cls):
        towns = Towns.query.all()
        towns_json = [town.serialize() for town in towns]
        return towns_json

    @classmethod
    def get_town_from_id(cls, id):
        town = cls.query.get(id)
        return town

    @classmethod
    def delete_town_from_id(cls, id):
        town = cls.get_town_from_id(id)
        if town is None:
            return None
        db.session.delete(town)
        db.session.commit()
        return town

    @classmethod
    def submit_town_from_json(cls, json_town):
        town = cls(town=json_town['town'], district=json_town.get("town", 0))
        db.session.add(town)
        db.session.commit()
        return town

    # todo:json encoding needed
    def serialize(self):
        json_town = {
            'id': self.id,
            'town': self.town,
        }
        return json_town
