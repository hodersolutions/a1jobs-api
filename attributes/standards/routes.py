##########################################################################
# Name:     Standards
# Purpose: File contains standard related routes
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
from attributes.standards.models import Standards
from attributes.standards.decorators import validate_standard

standards = Blueprint("standards", __name__)


@standards.route("/standards/all", methods=["GET"])
def api_standards_all():
    result = {
        "status": "success",
        "message": "Retrieved all standards successfully.",            
        "object": Standards.get_all_standards()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@standards.route("/standards", methods=["GET"])
def api_standards():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Standard, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    standard = Standards.get_standard_from_id(id)
    result = {
        "status": "success",
        "message": "Standard retrieved successfully.",            
        "standard": standard.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@standards.route("/standard/<int:id>", methods=["GET"])
def api_standard_via_id(id):
    standard = Standards.get_standard_from_id(id)
    if standard.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid standard."                
        }
        return Response(dumps(result), 400, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Standard retrieved successfully.",            
        "standard": standard.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@standards.route("/standards", methods=["POST"])
@validate_standard
def api_add_standard():
    request_data = request.get_json()
    standard = Standards.submit_standard_from_json(request_data)
    if standard is None or standard.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to add an Invalid Standard."
        }
        return Response(dumps(result), 500, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Standard added successfully.",
        "standard": standard.serialize()
    }
    return Response(dumps(result), 201, mimetype='application/json')