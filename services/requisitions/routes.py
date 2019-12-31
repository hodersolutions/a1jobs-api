from flask import Blueprint
from flask import Response, request
from json import dumps
from services.requisitions.models import Requisitions
# from services.requisitions.decorators import *
from flask_jwt_extended import (jwt_refresh_token_required)

requisitions = Blueprint('requisitions', __name__)

@requisitions.route("/api/v1/requisitions/filter", methods=["GET"])
def api_requisitions_all():
    filter_dict = request.args.to_dict()
    print(filter_dict)

    responseObject = {
        "status": "success",
        "message": "Retrieved all requisitions successfully.",
        "object": Requisitions.get_requisitions_by_filter(filter_dict)
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@requisitions.route("/api/v1/requisitions", methods=["GET"])
def api_requisitions():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Qualificaiton, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

    requisition = Requisitions.get_requisition_from_id(id)
    responseObject = {
        "status": "success",
        "message": "Requisition retrieved successfully.",
        "requisition": requisition.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@requisitions.route("/api/v1/requisition/<int:id>", methods=["GET"])
def api_requisition_via(id):
    requisition = Requisitions.query.get(id)
    if requisition.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid requisition."
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')
    responseObject = {
        "status": "success",
        "message": "Requisition retrieved successfully.",
        "requisition": requisition.serialize()
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')

@requisitions.route("/api/v1/requisitions", methods=["POST"])
#@token_required
def api_add_requisition():
    request_data = request.get_json()
    print(request_data)
    if(True):
        requisition = Requisitions.submit_requisition_from_json(request_data)
        if requisition is None or requisition.id < 0:
            responseObject = {
                "status": "failure",
                "message": "Failed to add an Invalid Requisition."
            }
            return Response(dumps(responseObject), 500, mimetype='application/json')
        responseObject = {
            "status": "success",
            "message": "Requisition added successfully.",
            "requisition": requisition.serialize()
        }
        return Response(dumps(responseObject), 201, mimetype='application/json')
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to add an Invalid Requisition."
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

#
@requisitions.route("/api/v1/requisition/<int:id>", methods=["DELETE"])
def api_delete_requisition_via(id):
    requisition = Requisitions.delete_requisition_from_id(id)
    if requisition is None or requisition.id < 0:
        responseObject = {
            "status": "failure",
            "message": "Failed to delete an Invalid Requisition."
        }
        return Response(dumps(responseObject), 404, mimetype='application/json')

    responseObject = {
        "status": "success",
        "message": "Requisition deleted successfully.",
        "requisition": requisition.serialize()
    }
    return Response(dumps(responseObject), 201, mimetype='application/json')