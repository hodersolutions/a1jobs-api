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


class DefaultConfig:
    """
    local dev environment
    """
    JWT_SECRET_KEY = 'vanvia-hoder-api'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///vanvia.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'
    DB_ADMIN_USER = 'vanvia-admin@vanvia.com'
    DB_ADMIN_PASSWORD = 'Vanvia@123'

    def __init__(self):
        pass


class StagingConfig(DefaultConfig):
    """
    staging environment variables
    """

    def __init__(self):
        pass


class ProductionConfig(DefaultConfig):
    """
    production environment config
    """

    def __init__(self):
        pass

