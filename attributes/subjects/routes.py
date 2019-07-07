##########################################################################
# Name:     Subjects
# Purpose: File contains subject related routes
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
from attributes.subjects.models import Subjects
from attributes.subjects.decorators import validate_subject

subjects = Blueprint("subjects", __name__)


@subjects.route("/subjects/all", methods=["GET"])
def api_subjects_all():
    result = {
        "status": "success",
        "message": "Retrieved all subjects successfully.",            
        "object": Subjects.get_all_subjects()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@subjects.route("/subjects", methods=["GET"])
def api_subjects():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid Subject, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    subject = Subjects.get_subject_from_id(id)
    result = {
        "status": "success",
        "message": "Subject retrieved successfully.",            
        "subject": subject.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@subjects.route("/subject/<int:id>", methods=["GET"])
def api_subject_via_id(id):
    subject = Subjects.get_subject_from_id(id)
    if subject.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid subject."                
        }
        return Response(dumps(result), 400, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Subject retrieved successfully.",            
        "subject": subject.serialize()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@subjects.route("/subjects", methods=["POST"])
@validate_subject
def api_add_subject():
    request_data = request.get_json()
    subject = Subjects.submit_subject_from_json(request_data)
    if subject is None or subject.id < 0:
        result = {
            "status": "failure",
            "message": "Failed to add an Invalid Subject."
        }
        return Response(dumps(result), 500, mimetype='application/json')
    result = {
        "status": "success",
        "message": "Subject added successfully.",
        "subject": subject.serialize()
    }
    return Response(dumps(result), 201, mimetype='application/json')