##########################################################################
# Name:     Users Routes
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
from services.users.models import Users
from roles.models import UserRoles, Roles
from services.users.decorators import validate_registration, validate_user_update
# from services.users.utils import add_user_and_role
from flask_jwt_extended import (jwt_refresh_token_required, get_jwt_identity)


users = Blueprint('users', __name__)


@users.route("/users/all", methods=["GET"])
# @jwt_refresh_token_required
def api_users_all():
    result = {
        "status": "success",
        "message": "Users found.",
        "user": Users.get_all_users()
    }
    return Response(dumps(result), 200, mimetype='application/json')


@users.route("/users/filter", methods=["GET"])
@jwt_refresh_token_required
def api_users_filter():
    filter_dict = request.args.to_dict()
    result = {
        "status": "success",
        "message": "Retrieved all profiles successfully.",
        "object": Users.get_users_by_filter(filter_dict)
    }
    return Response(dumps(result), 200, mimetype='application/json')


@users.route("/users/email", methods=["GET"])
@jwt_refresh_token_required
def api_user_by_email():
    if 'email' in request.args:
        email = request.args['email']
    else:
        result = {
            "status": "failure",
            "message": "Error: No email field provided. Please specify an username."
        }
        response = Response(dumps(result), 400, mimetype='application/json')
        return response

    user = Users.get_user_by_email(email)
    if not user:
        result = {
            "status": "failure",
            "message": "User not found.",
            "user": user
        }
    else:
        result = {
            "status": "success",
            "message": "User found.",
            "user": user
        }
    return Response(dumps(result), 200, mimetype='application/json')


@users.route("/users/mobile", methods=["GET"])
@jwt_refresh_token_required
def api_user_by_mobile():
    if 'mobile' in request.args:
        mobile = request.args['mobile']
    else:
        result = {
            "status": "failure",
            "message": "Error: No mobile field provided. Please specify an username."
        }
        response = Response(dumps(result), 400, mimetype='application/json')
        return response

    user = Users.get_user_by_mobile(mobile)
    if not user:
        result = {
            "status": "failure",
            "message": "User not found.",
            "user": user
        }
    else:
        result = {
            "status": "success",
            "message": "User found.",
            "user": user
        }
    return Response(dumps(result), 200, mimetype='application/json')


@users.route("/user/<int:uid>", methods=["GET"])
@jwt_refresh_token_required
def api_user_by_id(uid):
    user = Users.query.filter(ui=uid).first()
    # details =  user.details
    if not user:
        result = {
            "status": "failure",
            "message": "User not found.",
            "user": user
        }
    else:
        result = {
            "status": "success",
            "message": "User found.",
            "user": user.serialize()
        }
    return Response(dumps(result), 200, mimetype='application/json')


@users.route("/users/search/<string:text>", methods=["GET"])
@jwt_refresh_token_required
def api_users_by_text(text):
    user_list = Users.get_users_from_text(text)
    if not user_list:
        result = {
            "status": "failure",
            "message": "User not found.",
            "user": text
        }
    else:
        result = {
            "status": "success",
            "message": "User found.",
            "options": user_list
        }
    return Response(dumps(result), 200, mimetype='application/json')


@users.route("/users/email/exist", methods=["GET"])
@jwt_refresh_token_required
def api_user_by_email_exist():
    if 'email' in request.args:
        email = request.args['email']
    else:
        result = {
            "status": "no",
            "message": "Error: No email field provided. Please specify an email."
        }
        response = Response(dumps(result), 400, mimetype='application/json')
        return response

    user = Users.get_user_by_email(email)
    if not user:
        result = {
            "status": "no",
            "message": "User not found."
        }
    else:
        result = {
            "status": "yes",
            "message": "User found."
        }
    return Response(dumps(result), 200, mimetype='application/json')


@users.route("/user", methods=["POST"])
@validate_registration
def api_add_user():
    request_data = request.get_json()
    if "uid" in request_data:
        user = Users.get_user_by_uid(request_data["uid"])
        print(user)
        if user:
            result = {
                'status': 'success',
                'message': 'User Already exists with the uid.',
                'user': user.serialize()
            }
            response = Response(dumps(result), 200, mimetype='application/json')
            return response

    new_user = Users()
    if "uid" in request_data:
        new_user.uid = request_data["uid"]
    if "email" in request_data:
        new_user.email = request_data["email"]
    if "firstname" in request_data:
        new_user.first_name = request_data["firstname"]
    if "lastname" in request_data:
        new_user.last_name = request_data["lastname"]
    if "mobile" in request_data:
        new_user.mobile = request_data["mobile"]
    if "details" in request_data:
        new_user.details = request_data["details"]
    # new_user.created_user = get_jwt_identity().id

    success, error = Users.add_user(new_user)
    if success:
        # add the student role
        user_role = UserRoles(user=new_user.id, role=Roles.get_role(request.headers["role_keyword"]))
        UserRoles.add_user_role(user_role)
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

    return Response({h: 'hhf'}, 501, mimetype='application/json')


@users.route("/user", methods=["PUT"])
@validate_user_update
def api_update_user():
    request_data = request.get_json()
    user = Users.get_user_by_uid(request_data["uid"])

    if "uid" in request_data:
        user.uid = request_data["uid"]
    if "email" in request_data:
        user.email = request_data["email"]
    if "firstname" in request_data:
        user.first_name = request_data["firstname"]
    if "lastname" in request_data:
        user.last_name = request_data["lastname"]
    if "mobile" in request_data:
        user.mobile = request_data["mobile"]
    if "details" in request_data:
        user.details = request_data["details"]
    # new_user.created_user = get_jwt_identity().id

    success, error = user.update_user()
    if success:
        result = {
            'status': 'success',
            'message': 'Successfully updated.',
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

    return Response({h: 'hhf'}, 501, mimetype='application/json')

