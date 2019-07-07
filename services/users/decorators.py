##########################################################################
# Name:     validate
# Purpose: File contains all the decorators to validate the user request
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
from services.users.models import Users


def validate_registration(func):
    """
    The function should validate the user registration request
    :param func:
    :return: 400 and the error text
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        body = request.get_json()
        if "uid" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid uid."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        if "details" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter user details."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        if "details" in body and not body["details"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid user details."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        if "role" not in request.headers:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid role in header."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        if "role_keyword" in request.headers and not request.headers["role_keyword"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid user role."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        return func(*args, **kwargs)
    return wrapper


def validate_user_update(func):
    """
    The function should validate the user registration request
    :param func:
    :return: 400 and the error text
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        body = request.get_json()
        if "uid" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid uid."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        if "role_keyword" in request.headers and not request.headers["role_keyword"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid user role."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        request_data = request.get_json()
        if "uid" in request_data:
            user = Users.get_user_by_uid(request_data["uid"])
            if not user:
                result = {
                    'status': 'failure',
                    'message': 'User not found with the uid.',
                }
                response = Response(dumps(result), 400, mimetype='application/json')
                return response

        return func(*args, **kwargs)
    return wrapper
