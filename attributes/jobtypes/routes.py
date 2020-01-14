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
from attributes.jobtypes.models import JobTypes
from attributes.jobtypes.decorators import validate_job_type
from flask_jwt_extended import (jwt_refresh_token_required)


jobtypes = Blueprint('jobtypes', __name__)


@jobtypes.route("/api/v1/jobtypes/all", methods=["GET"])
# @jwt_refresh_token_required
def get_jobtypes_all():
    result = {
        "status": "success",
        "message": "JobTypes found.",
        "user": JobTypes.get_all_job_types()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@jobtypes.route("/api/v1/jobtypes", methods=["POST"])
@jwt_refresh_token_required
@validate_job_type
def api_add_role():
    request_data = request.get_json()
    jobtype = JobTypes()
    jobtype.name = request_data["name"]
    JobTypes.add_job_type(jobtype)
    result = {
        "status": "success",
        "message": "JobType Added.",
        "user": jobtype.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')