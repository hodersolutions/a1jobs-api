##########################################################################
# Name:     districts
# Purpose: File contains districs
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db


class Districts(db.Model):
    __tablename__ =  "districts"

    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(200), nullable=False)
    state = db.Column(db.Integer)

    def __repr__(self):
        return '{"id":{0}, "district":{1}}'.format(self.id, self.district)

    @classmethod
    def get_all_districts(cls):
        districts = Districts.query.all()
        districts_json = [district.serialize() for district in districts]
        return districts_json

    @classmethod
    def get_district_from_id(cls, id):
        district = cls.query.get(id)
        return district

    @classmethod
    def delete_district_from_id(cls, id):
        district = cls.get_district_from_id(id)
        if district is None:
            return None
        db.session.delete(district)
        db.session.commit()
        return district

    @classmethod
    def submit_district_from_json(cls, json_district):
        district = cls(district=json_district['district'], state=json_district.get("state", 0))
        db.session.add(district)
        db.session.commit()
        return district

    # todo:json encoding needed
    def serialize(self):
        json_district = {
            'id' : self.id ,
            'name' : self.district,
        }
        return json_district
