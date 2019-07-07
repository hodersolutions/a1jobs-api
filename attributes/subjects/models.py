##########################################################################
# Name:     Subject Decorators
# Purpose: File contains decorators for subject validations and Authentications
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db


class Subjects(db.Model):
    __tablename__ = "subjects"
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "subject":{1}}'.format(self.id, self.subject)

    @classmethod
    def get_all_subjects(cls):
        subjects = Subjects.query.all()
        subjects_json = [subject.serialize() for subject in subjects]
        return subjects_json

    @classmethod
    def get_subject_from_id(cls, id):
        subject = cls.query.get(id)
        return subject

    @classmethod
    def delete_subject_from_id(cls, id):
        subject = cls.get_subject_from_id(id)
        if subject is None:
            return None
        db.session.delete(subject)
        db.session.commit()
        return subject

    @classmethod
    def submit_subject_from_json(cls, json_subject):
        subject = cls(subject=json_subject['subject'])
        db.session.add(subject)
        db.session.commit()
        return subject

    # todo:json encoding needed
    def serialize(self):
        json_subject = {
            'id': self.id,
            'subject': self.subject,
        }
        return json_subject
