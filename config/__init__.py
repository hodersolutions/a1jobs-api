##########################################################################
# Name:     Config
# Purpose: File contains default config, staging config and production config
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
import os

class DefaultConfig:
    """
    local dev environment
    TODO: move this to a file, config.json?
    """
    JWT_SECRET_KEY = "a1jobs-hoder-api"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = "Content-Type"

    db_admin = {
        "user": "a1jobs-admin@hoder.in",
        "password": "A1jobs@123"
    }

    menu = {}

    permissions = {}

    sql_filters = {}

    def __init__(self):
        pass

    @classmethod
    def has_permission(cls, config, user_role, feature, action):
        if not config.permissions:
            return False
        if feature not in config.permissions[feature]:
            return False

        actions = config[feature]
        if action not in actions:
            return False

        roles = actions[action]
        roles_list = roles.split('|')

        if user_role in roles_list:
            return True

        if "all" in roles_list:
            return True

        return False

    @classmethod
    def get_features_for_role(cls, config, role):
        if not config.permissions:
            return None

        features = {}

        for feature, actions in config.permissions.items():
            action_list = []
            for action, roles in actions.items():
                roles_list = roles.split('|')

                if role in roles_list or "all" in roles_list:
                    action_list.append(action)

            if action_list:
                features[feature] = action_list

        return features


class StagingConfig(DefaultConfig):
    """
    staging environment variables
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    def __init__(self):
        pass


class ProductionConfig(DefaultConfig):
    """
    production environment config
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    def __init__(self):
        pass
