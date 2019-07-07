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
from flask import request, Response
from json import dumps
from flask import Blueprint
from attributes.institutions.models import Institutions
from attributes.institutions.decorators import validate_institution

institutions = Blueprint("institutions", __name__)


@institutions.route("/institutions/all", methods=["GET"])
def api_institutions_all():
    result = {
        "status": "success",
        "message": "Retrieved all institutions successfully.",
        "object": Institutions.get_all_institutions()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@institutions.route("/institutions", methods=["GET"])
def api_institutions():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Qualificaiton, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    institution = Institutions.get_institution_from_id(id)
    result = {
        "status": "success",
        "message": "Institution retrieved successfully.",
        "institution": institution.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@institutions.route("/institution/<int:id>", methods=["GET"])
def api_institution_via_id(id):
    institution = Institutions.get_institution_from_id(id)
    if institution.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid institution."
        }
        return Response(dumps(result), 400, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Institution retrieved successfully.",
        "institution": institution.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@institutions.route("/institutions", methods=["POST"])
@validate_institution
def api_add_institution():
    request_data = request.get_json()
    institution = Institutions.submit_institution_from_json(request_data)
    if institution is None or institution.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to add an Invalid Institution."
        }
        return Response(dumps(result), 500, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Institution added successfully.",
        "institution": institution.serialize()
    }
    return Response(dumps(result), 201, mimetype='application/json')


@institutions.route("/institution/<int:id>", methods=["DELETE"])
@validate_institution
def api_delete_institution_via_id(id):
    institution = Institutions.delete_institution_from(id)
    if institution is None or institution.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to delete an Invalid Institution."
        }
        return Response(dumps(result), 404, mimetype='application/json')

    result = {
        "status": "success",
        "message": "Institution deleted successfully.",
        "institution": institution.serialize()
    }
    return Response(dumps(result), 201, mimetype='application/json')
