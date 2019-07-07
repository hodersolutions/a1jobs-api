##########################################################################
# Name:     States
# Purpose: File contains state related routes
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################

from flask import request, Response
from flask import Blueprint
from json import dumps
from attributes.states.models import States
from attributes.states.decorators import validate_state

states = Blueprint("states", __name__)


@states.route("/states/all", methods=["GET"])
def api_states_all():
    result = {
        "status": "success",
        "message": "Retrieved all states successfully.",            
        "object": States.get_all_states()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@states.route("/states", methods=["GET"])
def api_states():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid State, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    state = States.get_state_from_id(id)
    result = {
        "status": "success",
        "message": "State retrieved successfully.",            
        "state": state.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@states.route("/state/<int:id>", methods=["GET"])
def api_state_via_id(id):
    state = States.get_state_from_id(id)
    if state.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid state."                
        }
        return Response(dumps(result), 400, mimetype='application/json')
    result = {
        "status": "success",
        "message": "State retrieved successfully.",            
        "state": state.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@states.route("/states", methods=["POST"])
@validate_state
def api_add_state():
    request_data = request.get_json()
    state = States.submit_state_from_json(request_data)
    if state is None or state.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to add an Invalid State."
        }
        return Response(dumps(result), 500, mimetype='application/json')
    result = {
        "status": "success",
        "message": "State added successfully.",
        "state": state.serialize()
    }
    return Response(dumps(result), 201, mimetype='application/json')


