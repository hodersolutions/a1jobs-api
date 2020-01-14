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
from attributes.roles.models import Roles


def validate_role(func):
    """
    The function should validate the user registration request
    :param func:
    :return: 400 and the error text
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        body = request.get_json()
        if "keyword" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter keyword."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        if "keyword" in body and not body["keyword"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid keyword."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        if Roles.get_role(body["keyword"]):
            result = {
                "status": "success",
                "message": "Role Already Exists."
            }
            return Response(dumps(result), 400, mimetype="application/json")
        return func(*args, **kwargs)
    return wrapper
