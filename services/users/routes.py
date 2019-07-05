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
from flask_jwt_extended import jwt_refresh_token_required


users = Blueprint('users', __name__)


@users.route("/users/all", methods=["GET"])
@jwt_refresh_token_required
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


@users.route("/user/<int:id>", methods=["GET"])
@jwt_refresh_token_required
def api_user_by_id(user_id):
    user = Users.query.get(user_id)
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
