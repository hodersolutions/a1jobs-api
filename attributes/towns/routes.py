from flask import request, Response, Blueprint
from attributes.towns.models import Towns
from attributes.towns.decorators import validate_town
from json import dumps


towns = Blueprint("towns", __name__)


@towns.route("/towns/all", methods=["GET"])
def api_towns_all():
    result = {
        "status": "success",
        "message": "Retrieved all towns successfully.",
        "question": Towns.get_all_towns()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@towns.route("/towns", methods=["GET"])
def api_towns():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Town, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    town = Towns.get_town_from_id(id)
    result = {
        "status": "success",
        "message": "Town retrieved successfully.",
        "town": town.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@towns.route("/town/<int:id>", methods=["GET"])
def api_town_via_id(id):
    town = Towns.get_town_from_id(id)
    if town.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid town."
        }
        return Response(dumps(result), 400, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Town retrieved successfully.",
        "town": town.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@towns.route("/towns", methods=["POST"])
@validate_town
def api_add_town():
    request_data = request.get_json()
    town = Towns.submit_town_from_json(request_data)
    if town is None or town.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to add an Invalid Town."
        }
        return Response(dumps(result), 500, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Town added successfully.",
        "town": town.serialize()
    }
    return Response(dumps(result), 201, mimetype='application/json')

