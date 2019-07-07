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


class States(db.Model):
    __tablename__ =  "states"

    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '{"id":{0}, "state":{1}}'.format(self.id, self.state)

    @classmethod
    def get_all_states(cls):
        states = States.query.all()
        states_json = [state.serialize() for state in states]
        return states_json

    @classmethod
    def get_state_from_id(cls, id):
        state = cls.query.get(id)
        return state

    @classmethod
    def delete_state_from_id(cls, id):
        state = cls.get_state_from_id(id)
        if state is None:
            return None
        db.session.delete(state)
        db.session.commit()
        return state

    @classmethod
    def submit_state_from_json(cls, json_state):
        state = cls(state=json_state['state'])
        db.session.add(state)
        db.session.commit()
        return state

    # todo:json encoding needed
    def serialize(self):
        json_state = {
            'id' : self.id ,
            'state' : self.state,
        }
        return json_state
