##########################################################################
# Name:     Reservations
# Purpose: File contains reservation related routes
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
from attributes.reservations.models import Reservations
from attributes.reservations.decorators import validate_reservation

reservations = Blueprint("reservations", __name__)


@reservations.route("/api/v1/reservations/all", methods=["GET"])
def api_reservations_all():
    result = {
        "status": "success",
        "message": "Retrieved all reservations successfully.",            
        "object": Reservations.get_all_reservations()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@reservations.route("/api/v1/reservations", methods=["GET"])
def api_reservations():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Reservation, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    reservation = Reservations.get_reservation_from_id(id)
    result = {
        "status": "success",
        "message": "Reservation retrieved successfully.",
        "reservation": reservation.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@reservations.route("/api/v1/reservation/<int:id>", methods=["GET"])
def api_reservation_via_id(id):
    reservation = Reservations.get_reservation_from_id(id)
    if reservation.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid reservation."                
        }
        return Response(dumps(result), 400, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Reservation retrieved successfully.",
        "reservation": reservation.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@reservations.route("/api/v1/reservations", methods=["POST"])
@validate_reservation
def api_add_reservation():
    request_data = request.get_json()
    reservation = Reservations.submit_reservation_from_json(request_data)
    if reservation is None or reservation.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to add an Invalid Reservation."
        }
        return Response(dumps(result), 500, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Reservation added successfully.",
        "reservation": reservation.serialize()
    }
    return Response(dumps(result), 201, mimetype='application/json')