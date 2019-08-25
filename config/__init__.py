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
    JWT_SECRET_KEY = "vanvia-hoder-api"
    SQLALCHEMY_DATABASE_URI = "sqlite:///vanvia.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CORS_HEADERS = "Content-Type"

    db_admin = {
        "user": "vanvia-admin@vanvia.com",
        "password": "Vanvia@123"
    }

    menu = {
        "student" : {
            "academics" : {
                "assignments" : "Assignments",
                "timetable" : "Time Table",
                "notebook": "Notebook",
                "performance": "Grades",
                "exams": "Exams",
                "attendance" : "Attendance",
                "courses" : "Courses",
                "competitions" : "Competitions",
                "certificates": "Certificates",
                "feedback" : "Feedback",
                "syllabus" : "Syllabus"
            },
            "finance" : {
                "fees" : "Fees",
                "transport" : "Transport Bills",
                "reimbursements" : "Re-Imbursements"
            },
            "facilities" : {
                "e-library" : "Library",
                "inventory" : "Inventory",
                "transport" : "Transport",
                "extracurricular" : "Extra Curricular"
            },
            "media" : {
                "events" : "Events",
                "alumni" : "Alumni",
                "newsletters" : "News Letters",
                "surveys" : "Survey",
                "galleries" : "Gallery"
            }
        },
        "staff" : {
            "work" : {
                "timetable" : "Time Table",
                "assignments" : "Assignments",
                "attendance" : "Attendance",
                "courses" : "Courses",
                "syllabus": "Syllabus",
                "exams": "Exams",
                "competitions" : "Competitions",
                "ptc" : "Parent Teacher Incidents"
            },
            "finance": {
                "salary": "Salary",
                "transport": "Transport Bills",
                "expenses": "Expenses",
                "funds": "Funds"
            },
            "facilities": {
                "e-library": "Library",
                "inventory": "Inventory",
                "transport": "Transport",
                "extracurricular": "Extra Curricular"
            },
            "media": {
                "events": "Events",
                "alumni": "Alumni",
                "newsletters": "News Letters",
                "surveys": "Survey",
                "galleries": "Gallery",
                "moms": "Minutes of Meetings",
                "activities" : "Activities Log"
            }
        },
        "parent" : {
            "academics": {
                "assignments": "Assignments",
                "ptc": "Incidents",
                "timetable": "Time Table",
                "notebook": "Notebook",
                "performance": "Grades",
                "exams": "Exams",
                "attendance": "Attendance",
                "courses": "Courses",
                "competitions": "Competitions",
                "certificates": "Certificates",
                "feedback": "Feedback",
                "syllabus": "Syllabus"
            },
            "finance": {
                "fees": "Fees",
                "transport": "Transport Bills",
                "reimbursements": "Re-Imbursements"
            },
            "facilities": {
                "e-library": "Library",
                "inventory": "Inventory",
                "transport": "Transport",
                "extracurricular": "Extra Curricular"
            },
            "media": {
                "events": "Events",
                "alumni": "Alumni",
                "newsletters": "News Letters",
                "surveys": "Survey",
                "galleries": "Gallery"
            }
        },
        "principal": {
            "staff" : {
                "timetable": "Time Table",
                "attendance": "Attendance",
                "courses": "Courses",
                "syllabus": "Syllabus",
                "exams": "Exams",
                "competitions": "Competitions",
                "ptc": "Parent Teacher Incidents"
            },
            "students" : {
                "assignments": "Assignments",
                "timetable": "Time Table",
                "notebook": "Notebook",
                "performance": "Grades",
                "exams": "Exams",
                "attendance": "Attendance",
                "courses": "Courses",
                "competitions": "Competitions",
                "certificates": "Certificates",
                "feedback": "Feedback",
                "syllabus": "Syllabus",

            }
        },
        "admin": {
            "staff": {
                "create-staff": "Enrollment",
                "timetable": "Time Table",
                "attendance": "Attendance",
                "courses": "Courses",
                "syllabus": "Syllabus",
                "exams": "Exams",
                "competitions": "Competitions",
                "ptc": "Parent Teacher Incidents"
            },
            "students": {
                "create-student": "Enrollment",
                "performance": "Grades",
                "exams": "Exams",
                "attendance": "Attendance",
                "courses": "Courses",
                "competitions": "Competitions",
                "certificates": "Certificates",
                "feedback": "Feedback",
                "syllabus": "Syllabus",

            },
            "finance": {
                "fees": "Fees",
                "transport": "Transport Bills",
                "reimbursements": "Re-Imbursements"
            },
            "facilities": {
                "e-library": "Library",
                "inventory": "Inventory",
                "transport": "Transport",
                "extracurricular": "Extra Curricular"
            },
            "media": {
                "events": "Events",
                "alumni": "Alumni",
                "newsletters": "News Letters",
                "surveys": "Survey",
                "galleries": "Gallery"
            }
        }

    }
    
    permissions = {
        "student": {
            "create": "admin|management|principal|staff",
            "view": "admin|management|principal|staff|student|parent",
            "modify": "admin|management|principal|student"
        },
        "salary": {
            "create": "admin",
            "view": "admin|management|principal|staff",
            "modify": "admin"
        },
        "student_performance": {
            "create": "admin|principal|staff",
            "view": "admin|management|principal|staff|student",
            "modify": "admin|principal|staff"
        },
        "student_attendance": {
            "create": "admin|management|principal|staff|",
            "view": "admin|management|principal|staff|student|parent",
            "modify": "admin|management|principal|staff|"
        },
        "staff_attendance": {
            "create": "admin|principal|",
            "view": "admin|management|principal|staff|",
            "modify": "admin|principal|"
        },
        "fees": {
            "create": "admin|principal|",
            "view": "admin|management|principal|staff|student|parent",
            "modify": "admin|principal|"
        },
        "expenses": {
            "create": "admin|management|principal|staff|student",
            "view": "admin|management|principal|staff|student",
            "approve": "admin"
        },
        "reimbursements": {
            "create": "",
            "view": "",
            "modify": ""
        },
        "feedback": {
            "create": "admin|management|principal",
            "view": "admin|management|principal",
            "provide": "management|student"
        },
        "newsletter": {
            "create": "admin|management|principal",
            "view": "admin|management|principal|staff|student"
        },
        "alumni": {
            "create": "admin|management|principal",
            "view": "admin|management|principal|staff|student|parent"
        },
        "library": {
            "create": "admin|principal|staff",
            "view": "admin|management|principal|staff|student|parent",
            "modify": "admin|principal|staff"
        },
        "inventory": {
            "create": "admin|principal|staff",
            "view": "admin|management|principal|staff",
            "modify": "admin|principal"
        },
        "funds": {
            "create": "admin|principal|staff",
            "view": "admin|management|principal|staff",
            "modify": "admin|principal"
        },
        "events": {
            "create": "admin|principal|management",
            "view": "admin|management|principal|staff|student|parent",
            "modify": "admin|principal|management",
            "delete": "admin|principal|management"
        },
        "mom": {
            "create": "admin|principal|management",
            "view": "admin|management|principal|staff",
            "modify": "admin|principal|management"
        },
        "performance": {
            "create": "admin|management|principal|staff",
            "view": "admin|management|principal|staff|student|parent",
            "modify": "admin|management|principal|staff"
        },
        "staff": {
            "create": "admin|management|principal",
            "view": "admin|management|principal|staff",
            "modify": "admin|management|principal",
            "delete": "admin|management|principal"
        },
        "courses": {
            "create": "admin|management|principal|staff",
            "view": "admin|management|principal|staff",
            "modify": "admin|management|principal|staff"
        },
        "survey": {
            "create": "admin|management",
            "view": "admin|management|principal|staff|student|parent",
            "participate": "admin|management|principal|staff|student|parent"
        },
        "gallery": {
            "create": "admin|management|principal",
            "view": "admin|management|principal|staff|student|parent",
            "modify": "admin|management|principal"
        }}

    sql_filters = {
        "student" : {
            "student" : {
                "query": """select users.* from users inner join user_roles on 
                        users.id = user_roles.user where uid = {} and user_roles.role = {}""",
                "filter" : ["uid", "role"]
            },
            "staff" : "select * from users where institution = {}",
            "principal" : "institution = {}",
            "management" : "1=1",
            "admin": "1=1",
            "parent" : "uid in {}"
        },
        "staff" : {
            "student" : "1=0",
            "staff" : "uid = {}",
            "principal" : "institution = {}",
            "managment" : "1=1",
            "admin": "1=1",
            "parent" : "1=0"
        },
        "principal" : {
            "student" : "1=0",
            "staff" : "1=0",
            "principal": "uid = {}"
        }
    }

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

    def __init__(self):
        pass


class ProductionConfig(DefaultConfig):
    """
    production environment config
    """

    def __init__(self):
        pass