##########################################################################
# Name:     Religions
# Purpose: File contains religion related routes
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
from attributes.religions.models import Religions
from attributes.religions.decorators import validate_religion

religions = Blueprint("religions", __name__)


@religions.route("/religions/all", methods=["GET"])
def api_religions_all():
    result = {
        "status": "success",
        "message": "Retrieved all religions successfully.",            
        "object": Religions.get_all_religions()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@religions.route("/religions", methods=["GET"])
def api_religions():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Religion, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    religion = Religions.get_religion_from_id(id)
    result = {
        "status": "success",
        "message": "Religion retrieved successfully.",            
        "religion": religion.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@religions.route("/religion/<int:id>", methods=["GET"])
def api_religion_via_id(id):
    religion = Religions.get_religion_from_id(id)
    if religion.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid religion."                
        }
        return Response(dumps(result), 400, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Religion retrieved successfully.",            
        "religion": religion.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@religions.route("/religions", methods=["POST"])
@validate_religion
def api_add_religion():
    request_data = request.get_json()
    religion = Religions.submit_religion_from_json(request_data)
    if religion is None or religion.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to add an Invalid Religion."
        }
        return Response(dumps(result), 500, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Religion added successfully.",
        "religion": religion.serialize()
    }
    return Response(dumps(result), 201, mimetype='application/json')