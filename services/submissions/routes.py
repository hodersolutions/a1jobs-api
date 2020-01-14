##########################################################################
# Name:     Job Applications
# Purpose: File contains Users
#
# Author:     Kalyana Krishna Varanasi
#
# Created:   05/01/2020
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import request, Response, Blueprint
from services.submissions.models import JobApplications
from json import dumps

jobapplications = Blueprint('jobapplications', __name__)

@jobapplications.route("/api/v1/jobapplications/all", methods=["GET"])
def api_districts_all():
    result = {
        "status": "success",
        "message": "Retrieved all job applications successfully.",
        "object": JobApplications.get_all_applications()
    }
    return Response(dumps(result), 200, mimetype='application/json')

@jobapplications.route("/api/v1/jobapplications", methods=["POST"])
def api_add_job_application():
    request_data = request.get_json()
    application = JobApplications.submit_application_from_json(request_data)
    if application is None or application.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to add an job application."
        }
        return Response(dumps(result), 500, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Job applied successfully."
    }
    return Response(dumps(result), 201, mimetype='application/json')