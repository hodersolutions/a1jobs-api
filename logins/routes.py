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
from logins.models import Users, UsersProfileBasic
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
    
    success, error = Users.add_user(request_data)
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
        "message": "Failed to Login, please check your email / mobile and password."
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
#----------------------------User Profile Basic-----------------------------------------#

@logins.route("/api/v1/profile", methods=["POST"])
#@token_required
def api_add_profile():
    request_data = request.get_json()
    if(True):
        profile, error = UsersProfileBasic.add_or_update_user_by_userid(request_data)        
        if error or profile is None or profile.id < 0:
            print(error)
            responseObject = {
                "status": "failure",
                "message": "Failed to add / update an Invalid Profile."
            }
            return Response(dumps(responseObject), 500, mimetype='application/json')
        responseObject = {
            "status": "success",
            "message": "Profile added / updated successfully."            
        }
        return Response(dumps(responseObject), 201, mimetype='application/json')
    else:
        responseObject = {
            "status": "failure",
            "message": "Failed to add / update an Invalid Profile."
        }
        return Response(dumps(responseObject), 400, mimetype='application/json')

@logins.route("/api/v1/profile", methods=["GET"])
def api_get_profile():
    userid = 0
    if 'userid' in request.args:
        userid = int(request.args['userid'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid user, no (userid) field provided. please specify an (userid)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    if userid < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid user."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    profile, error = UsersProfileBasic.get_user_profile_by_userid(userid)

    if profile is None:
        result = {
            "status": "failure",
            "message": "User Profile is incomplete, please update."            
        }
        return Response(dumps(result), 400, mimetype='application/json')
    else:
        profile_serialized = profile.serialize()
        result = {
            "status": "success",
            "message": "User Profile retrieved successfully.",
            "profile": profile_serialized
        }
        return Response(dumps(result), 200, mimetype='application/json')

@logins.route("/api/v1/profile/user", methods=["GET"])
def api_get_profile_via_userid():
    userid = 0
    if 'userid' in request.args:
        userid = int(request.args['userid'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid user, no (userid) field provided. please specify an (userid)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    if userid < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid user."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    profile = UsersProfileBasic.get_profile_joining_user_via_userid(userid)

    if profile is None:
        result = {
            "status": "failure",
            "message": "User Profile is incomplete, please update."            
        }
        return Response(dumps(result), 400, mimetype='application/json')
    else:
        result = {
            "status": "success",
            "message": "User Profile retrieved successfully.",
            "profile": profile
        }
        return Response(dumps(result), 200, mimetype='application/json')

@logins.route("/api/v1/profile/id", methods=["GET"])
def api_get_profile_by_id():
    id = 0
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid user profile, no (id) field provided. please specify an (id)."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    if id < 0:
        result = {
            "status": "failure",
            "message": "Failed to retrieve an Invalid user  profile."
        }
        return Response(dumps(result), 400, mimetype='application/json')

    profile = UsersProfileBasic.get_userprofile_joining_user(id)

    if profile is None:
        result = {
            "status": "failure",
            "message": "User Profile does not exist."            
        }
        return Response(dumps(result), 400, mimetype='application/json')
    else:
        result = {
            "status": "success",
            "message": "User Profile retrieved successfully.",
            "profile": profile
        }
        return Response(dumps(result), 200, mimetype='application/json')


@logins.route("/api/v1/profile/filter", methods=["GET"])
def api_get_all_profiles():
    profile_dict = request.args.to_dict()
    responseObject = {
        "status": "success",
        "message": "Retrieved all user profiles successfully.",
        "users": UsersProfileBasic.get_all_user_profiles(profile_dict)
    }
    return Response(dumps(responseObject), 200, mimetype='application/json')
