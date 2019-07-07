##########################################################################
# Name:     Castes
# Purpose: File contains caste related routes
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
from attributes.castes.models import Castes
from attributes.castes.decorators import validate_caste

castes = Blueprint("castes", __name__)


@castes.route("/castes/all", methods=["GET"])
def api_castes_all():
    result = {
        "status": "success",
        "message": "Retrieved all castes successfully.",            
        "object": Castes.get_all_castes()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@castes.route("/castes", methods=["GET"])
def api_castes():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Caste, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    caste = Castes.get_caste_from_id(id)
    result = {
        "status": "success",
        "message": "Caste retrieved successfully.",            
        "caste": caste.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@castes.route("/caste/<int:id>", methods=["GET"])
def api_caste_via_id(id):
    caste = Castes.get_caste_from_id(id)
    if caste.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid caste."                
        }
        return Response(dumps(result), 400, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Caste retrieved successfully.",            
        "caste": caste.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@castes.route("/castes", methods=["POST"])
@validate_caste
def api_add_caste():
    request_data = request.get_json()
    caste = Castes.submit_caste_from_json(request_data)
    if caste is None or caste.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to add an Invalid Caste."
        }
        return Response(dumps(result), 500, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Caste added successfully.",
        "caste": caste.serialize()
    }
    return Response(dumps(result), 201, mimetype='application/json')