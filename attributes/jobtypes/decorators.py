##########################################################################
# Name:     validate
# Purpose: File contains all the decorators to validate the request
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import request, Response
from json import dumps
from functools import wraps
from attributes.jobtypes.models import JobTypes


def validate_job_type(func):
    """
    The function should validate the user registration request
    :param func:
    :return: 400 and the error text
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        body = request.get_json()
        if "name" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter name."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        if "name" in body and not body["name"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid name."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        if JobTypes.get_job_type(body["name"]):
            result = {
                "status": "success",
                "message": "Name Already Exists."
            }
            return Response(dumps(result), 400, mimetype="application/json")
        return func(*args, **kwargs)
    return wrapper
