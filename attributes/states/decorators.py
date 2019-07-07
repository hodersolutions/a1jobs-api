##########################################################################
# Name:     State Decorators
# Purpose: File contains decorators for state validations and Authentications
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


def validate_state(func):
    """
        The function should validate the district registration request
        :param func:
        :return: 400 and the error text
        """

    @wraps(func)
    def wrapper(*args, **kwargs):
        body = request.get_json()
        if "state" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid state."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        if "state" in body and not body["state"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid state."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        return func(*args, **kwargs)
    return wrapper
