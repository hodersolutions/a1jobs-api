##########################################################################
# Name:     Qualifications
# Purpose: File contains qualification related routes
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
from attributes.qualifications.models import Qualifications
from attributes.qualifications.decorators import validate_qualification

qualifications = Blueprint("qualifications", __name__)


@qualifications.route("/api/v1/qualifications/all", methods=["GET"])
def api_qualifications_all():
    result = {
        "status": "success",
        "message": "Retrieved all qualifications successfully.",            
        "object": Qualifications.get_all_qualifications()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@qualifications.route("/api/v1/qualifications", methods=["GET"])
def api_qualifications():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Qualification, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    qualification = Qualifications.get_qualification_from_id(id)
    result = {
        "status": "success",
        "message": "Qualification retrieved successfully.",            
        "qualification": qualification.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@qualifications.route("/api/v1/qualification/<int:id>", methods=["GET"])
def api_qualification_via_id(id):
    qualification = Qualifications.get_qualification_from_id(id)
    if qualification.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid qualification."                
        }
        return Response(dumps(result), 400, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Qualification retrieved successfully.",            
        "qualification": qualification.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@qualifications.route("/api/v1/qualifications", methods=["POST"])
@validate_qualification
def api_add_qualification():
    request_data = request.get_json()
    qualification = Qualifications.submit_qualification_from_json(request_data)
    if qualification is None or qualification.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to add an Invalid Qualification."
        }
        return Response(dumps(result), 500, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Qualification added successfully.",
        "qualification": qualification.serialize()
    }
    return Response(dumps(result), 201, mimetype='application/json')