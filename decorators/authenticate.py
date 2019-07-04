##########################################################################
# Name:     authenticate
# Purpose: This file is to have all the decorators to authenticate a request
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


def authenticate_token(func):
    @wraps(func)
	def wrapper(*args, **kwargs):
		if "token" in request.headers and "email" in request.headers:
			token = request.headers['token']
			email = request.headers['email']
			try:
				decode(token, email)
				return f(*args, **kwargs)
			except:
				errorObj = {
					"status": "failure",
					"message": "Invalid access, please login first to access this request."
				}
				return Response(dumps(errorObj), 401, mimetype="application/json")
		else:
			errorObj = {
				"status": "failure",
				"message": "Invalid access, please login first to access this request."
			}
			return Response(dumps(errorObj), 401, mimetype="application/json")
	return wrapper