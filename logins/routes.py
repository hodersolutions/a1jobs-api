##########################################################################
# Name:     login Routes
# Purpose: File contains User request endpoints like register, login, logout etc.
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import Blueprint
from flask import Response, request
from json import dumps
from logins.decorators import validate_login
from logins.models import Users
from flask_jwt_extended import (create_refresh_token, jwt_refresh_token_required)


logins = Blueprint('logins', __name__)

@logins.route('/api/v1/register', methods=["POST"])
@validate_login
def register():
    request_data = request.get_json()
    if "email" in request_data:
        user = Users.get_user_by_email(request_data["email"])
        if user:
            result = {
                'status': 'failure',
                'message': 'User Already exists with the Email.'
            }
            response = Response(dumps(result), 400, mimetype='application/json')
            return response
    if "mobile" in request_data:
        user = Users.get_user_by_mobile(request_data["mobile"])
        if user:
            result = {
                'status': 'failure',
                'message': 'User Already exists with the Mobile.'
            }
            response = Response(dumps(result), 400, mimetype='application/json')
            return response

    new_user = Users()

    if "email" in request_data:
        new_user.email = request_data["email"]
    if "mobile" in request_data:
        new_user.mobile = request_data["mobile"]
    if "password" in request_data:
        new_user.password = Users.generate_hash(request_data["password"])
    # new_user.created_user = get_jwt_identity().id

    success, error = Users.add_user(new_user)
    if success:
        result = {
            'status': 'success',
            'message': 'Successfully registered.',
            'user': success
        }
        response = Response(dumps(result), 201, mimetype='application/json')
        return response
    if error:
        result = {
            'status': 'failure',
            'message': 'Internal Error.',
            'user': {'msg': str(error)}
        }
        response = Response(dumps(result), 501, mimetype='application/json')
        return response

@logins.route('/api/v1/login', methods=["POST"])
@validate_login
def login():
    request_data = request.get_json()
    user = None
    if "email" in request_data:
        user = Users.query.filter_by(email=request_data["email"]).first()
    if not user and "mobile" in request_data:
        user = Users.query.filter_by(mobile=request_data["mobile"]).first()
    if not user or not user.password:
        result = {
            'status': 'failure',
            'message': 'User is not registered.'
        }
        response = Response(dumps(result), 404, mimetype='application/json')
        return response

    if user and user.verify_hash(request_data['password'], user.password):
        access_token = create_refresh_token(identity=user.id)
        result = {
            'status': 'success',
            'message': 'User logged in.',
            'user': user.serialize(),
            'access_token': access_token
        }
        response = Response(dumps(result), 200, mimetype='application/json')
        return response
    result = {
        "status": "failure",
        "message": "Failed to Login"
    }
    return Response(dumps(result), 401, mimetype="application/json")


@logins.route('/api/v1/logout', methods=["POST"])
@jwt_refresh_token_required
def logout():
    result = {
        "status": "success",
        "message": "User logged out."
    }
    return Response(dumps(result), 201, mimetype="application/json")