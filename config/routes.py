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
from config import DefaultConfig
from config.decorators import validate_config, authorize_config

config = Blueprint('config', __name__)


@config.route("/api/v1/config/role", methods=["GET"])
@validate_config
def get_config_for_role():
    header = request.headers
    result = {
        "status": "success",
        "message": "Config retrieved.",
        header["role_keyword"]: DefaultConfig.get_features_for_role(DefaultConfig(), header["role_keyword"])
    }
    return Response(dumps(result), 200, mimetype='application/json')


@config.route("/api/v1/config/haspermission/<string:feature>/<string:action>", methods=["GET"])
@validate_config
@authorize_config
def get_config_permission_for_role(feature, action):
    result = {
        "status": "success",
        "message": "Has Permissions."
    }
    return Response(dumps(result), 200, mimetype='application/json')


@config.route("/api/v1/config/all", methods=["GET"])
def get_config_all():
    result = {
        "status": "success",
        "message": "Config retrieved.",
        "admin": DefaultConfig().permissions
    }
    return Response(dumps(result), 200, mimetype='application/json')


@config.route("/api/v1/config/menu", methods=["GET"])
@validate_config
def get_config_menu():
    header = request.headers
    result = {
        "status": "success",
        "message": "Config retrieved.",
        "menu": DefaultConfig().menu[header["role_keyword"]]
    }
    return Response(dumps(result), 200, mimetype='application/json')