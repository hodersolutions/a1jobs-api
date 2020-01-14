##########################################################################
# Name: main
# Purpose: main module which creates the Application instance
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from logins.models import Users
from attributes.roles.models import (Roles, UserRoles)
from flask import Response
from json import dumps


def add_user_and_role(request_data, keyword):
    if "email" in request_data:
        user = Users.get_user_by_email(request_data["email"])
        if user:
            result = {
                'status': 'success',
                'message': 'User Already exists with the email.',
                'user': user.serialize()
            }
            response = Response(dumps(result), 200, mimetype='application/json')
            return response

    if "mobile" in request_data:
        user = Users.get_user_by_mobile(request_data["mobile"])
        if user:
            result = {
                'status': 'success',
                'message': 'User Already exists with the mobile.',
                'user': user.serialize()
            }
            response = Response(dumps(result), 200, mimetype='application/json')
            return response

    new_user = Users()
    if "email" in request_data:
        new_user.email = request_data["email"]
    if "firstname" in request_data:
        new_user.first_name = request_data["firstname"]
    if "lastname" in request_data:
        new_user.last_name = request_data["lastname"]
    if "mobile" in request_data:
        new_user.mobile = request_data["mobile"]
    # new_user.created_user = get_jwt_identity().id

    success, error = Users.add_user(new_user)
    if success:
        # add the student role
        user_role = UserRoles(user=new_user.id, role=Roles.get_role(keyword))
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