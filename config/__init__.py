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
    TODO: move this to a file, config.json?
    """
    JWT_SECRET_KEY = 'vanvia-hoder-api'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///vanvia.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = 'Content-Type'

    db_admin = {
        'user': 'vanvia-admin@vanvia.com',
        'password': 'Vanvia@123'
    }
    admin_student = {
        'create': 'admin|management|principal|staff',
        'view': 'admin|management|principal|staff|student|parent',
        'modify': 'admin|management|principal|student'
    }
    admin_salary = {
        'create': 'admin',
        'view': 'admin|management|principal|staff',
        'modify': 'admin'
    }
    admin_student_performance = {
        'create': 'admin|principal|staff',
        'view': 'admin|management|principal|staff|student',
        'modify': 'admin|principal|staff'
    }
    admin_student_attendance = {
        'create': 'admin|management|principal|staff|',
        'view': 'admin|management|principal|staff|student|parent',
        'modify': 'admin|management|principal|staff|'
    }
    admin_staff_attendance = {
        'create': 'admin|principal|',
        'view': 'admin|management|principal|staff|',
        'modify': 'admin|principal|'
    }
    admin_student_fees = {
        'create': 'admin|principal|',
        'view': 'admin|management|principal|staff|student|parent',
        'modify': 'admin|principal|'
    }
    admin_expenses = {
        'create': 'admin|management|principal|staff|student',
        'view': 'admin|management|principal|staff|student',
        'approve': 'admin'
    }
    admin_reimbursements = {
        'create': '',
        'view': '',
        'modify': ''
    }
    admin_feedback = {
        'create': 'admin|management|principal',
        'view': 'admin|management|principal',
        'provide': 'management|student'
    }
    admin_newsletter = {
        'create': 'admin|management|principal',
        'view': 'admin|management|principal|staff|student'
    }
    admin_alumni = {
        'create': 'admin|management|principal',
        'view': 'admin|management|principal|staff|student|parent'
    }
    admin_library = {
        'create': 'admin|principal|staff',
        'view': 'admin|management|principal|staff|student|parent',
        'modify': 'admin|principal|staff'
    }
    admin_inventory = {
        'create': 'admin|principal|staff',
        'view': 'admin|management|principal|staff',
        'modify': 'admin|principal'
    }
    admin_funds = {
        'create': 'admin|principal|staff',
        'view': 'admin|management|principal|staff',
        'modify': 'admin|principal'
    }
    admin_events = {
        'create': 'admin|principal|management',
        'view': 'admin|management|principal|staff|student|parent',
        'modify': 'admin|principal|management',
        'delete': 'admin|principal|management'
    }
    admin_mom = {
        'create': 'admin|principal|management',
        'view': 'admin|management|principal|staff',
        'modify': 'admin|principal|management'
    }
    admin_performance = {
        'create': 'admin|management|principal|staff',
        'view': 'admin|management|principal|staff|student|parent',
        'modify': 'admin|management|principal|staff'
    }
    admin_staff_enroll = {
        'create': 'admin|management|principal',
        'view': 'admin|management|principal|staff',
        'modify': 'admin|management|principal',
        'delete': 'admin|management|principal'
    }
    admin_courses_enroll = {
        'create': 'admin|management|principal|staff',
        'view': 'admin|management|principal|staff',
        'modify': 'admin|management|principal|staff'
    }
    admin_survey = {
        'create': 'admin|management',
        'view': 'admin|management|principal|staff|student|parent',
        'participate': 'admin|management|principal|staff|student|parent'
    }
    admin_gallery = {
        'create': 'admin|management|principal',
        'view': 'admin|management|principal|staff|student|parent',
        'modify': 'admin|management|principal'
    }

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

