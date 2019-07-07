##########################################################################
# Name:     Users
# Purpose: File contains Users
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import request, Response, Blueprint
from attributes.districts.models import Districts
from attributes.districts.decorators import validate_district
from json import dumps

districts = Blueprint('districts', __name__)


@districts.route("/districts/all", methods=["GET"])
def api_districts_all():
    result = {
        "status": "success",
        "message": "Retrieved all districts successfully.",
        "object": Districts.get_all_districts()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@districts.route("/districts", methods=["GET"])
def api_districts():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid District, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    district = Districts.get_district_from_id(id)
    result = {
        "status": "success",
        "message": "District retrieved successfully.",
        "district": district.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@districts.route("/district/<int:district_id>", methods=["GET"])
def api_district_via_id(district_id):
    district = Districts.get_district_from_id(district_id)
    if district.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid district."
        }
        return Response(dumps(result), 400, mimetype='application/json')
    result = {
        "status": "success",
        "message": "District retrieved successfully.",
        "district": district.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@districts.route("/district", methods=["POST"])
@validate_district
def api_add_district():
    request_data = request.get_json()
    district = Districts.submit_district_from_json(request_data)
    if district is None or district.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to add an Invalid District."
        }
        return Response(dumps(result), 500, mimetype='application/json')
    result = {
        "status": "success",
        "message": "District added successfully.",
        "district": district.serialize()
    }
    return Response(dumps(result), 201, mimetype='application/json')