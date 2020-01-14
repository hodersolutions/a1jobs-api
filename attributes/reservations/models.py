##########################################################################
# Name:     Reservation Decorators
# Purpose: File contains decorators for reservation validations and Authentications
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import db


class Reservations(db.Model):
    __tablename__ = "reservations"
    id = db.Column(db.Integer, primary_key=True)
    reservation = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "reservation":{1}}'.format(self.id, self.reservation)

    @classmethod
    def get_all_reservations(cls):
        reservations = Reservations.query.all()
        reservations_json = [reservation.serialize() for reservation in reservations]
        return reservations_json

    @classmethod
    def get_reservation_from_id(cls, id):
        reservation = cls.query.get(id)
        return reservation

    @classmethod
    def delete_reservation_from_id(cls, id):
        reservation = cls.get_reservation_from_id(id)
        if reservation is None:
            return None
        db.session.delete(reservation)
        db.session.commit()
        return reservation

    @classmethod
    def submit_reservation_from_json(cls, json_reservation):
        reservation = cls(reservation=json_reservation['reservation'])
        db.session.add(reservation)
        db.session.commit()
        return reservation

    # todo:json encoding needed
    def serialize(self):
        json_reservation = {
            'id': self.id,
            'reservation': self.reservation,
        }
        return json_reservation
