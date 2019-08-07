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


def validate_login(func):
    """
    The function should validate the user registration request
    :param func:
    :return: 400 and the error text
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        body = request.get_json()
        if "uid" not in body and "mobile" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid credentials."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        if "uid" in body and not body["uid"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid uid."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        if "password" in body and not body["password"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid password."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        return func(*args, **kwargs)
    return wrapper
