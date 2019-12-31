##########################################################################
# Name:     qualification Decorators
# Purpose: File contains decorators for qualification validations and Authentications
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


def validate_qualification(func):
    """
        The function should validate the district registration request
        :param func:
        :return: 400 and the error text
        """

    @wraps(func)
    def wrapper(*args, **kwargs):
        body = request.get_json()
        if "qualification" not in body:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid Qualification."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        if "qualification" in body and not body["qualification"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Please enter valid Qualification."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        return func(*args, **kwargs)
    return wrapper
