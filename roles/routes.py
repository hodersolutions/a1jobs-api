##########################################################################
# Name:     Roles Routes
# Purpose: File contains User request endpoints like 'add role', 'get role' and 'assign a role to user'
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import Blueprint
from flask import Response, request
from json import dumps
from roles.models import Roles
from roles.decorators import validate_role
from flask_jwt_extended import (jwt_refresh_token_required, get_jwt_identity)


roles = Blueprint('roles', __name__)


@roles.route("/roles/all", methods=["GET"])
@jwt_refresh_token_required
def get_roles_all():
    result = {
        "status": "success",
        "message": "Roles found.",
        "user": Roles.get_all_roles()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@roles.route("/roles", methods=["POST"])
@jwt_refresh_token_required
@validate_role
def api_add_role():
    request_data = request.get_json()
    role = Roles()
    role.keyword = request_data["keyword"]
    if "description" in request_data:
        role.description = request_data["description"]
    Roles.add_role(role)
    result = {
        "status": "success",
        "message": "Role Added.",
        "user": role.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')



