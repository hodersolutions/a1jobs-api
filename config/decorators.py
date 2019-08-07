##########################################################################
# Name:     Config validators
# Purpose: File contains all the decorators to validate the config request
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
from config import DefaultConfig


def validate_config(func):
    """
        The function should validate the user registration request
        :param func:
        :return: 400 and the error text
        """

    @wraps(func)
    def wrapper(*args, **kwargs):
        headers = request.headers
        if "role_keyword" not in headers:
            error = {
                "status": "failure",
                "message": "Bad Input, Missing Headers 'role_keyword'."
            }
            return Response(dumps(error), 400, mimetype="application/json")

        if not headers["role_keyword"]:
            error = {
                "status": "failure",
                "message": "Bad Input, Missing Headers 'role_keyword'."
            }
            return Response(dumps(error), 400, mimetype="application/json")
        return func(*args, **kwargs)
    return wrapper


def authorize_config(func):
    """
            The function should validate the user registration request
            :param func:
            :return: 400 and the error text
            """

    @wraps(func)
    def wrapper(*args, **kwargs):
        headers = request.headers
        if not DefaultConfig.has_permission(DefaultConfig(), headers["role_keyword"], args[0], args[1]):
            error = {
                "status": "failure",
                "message": "Un-Authorized permission for the action."
            }
            return Response(dumps(error), 401, mimetype="application/json")
        return func(*args, **kwargs)

    return wrapper
