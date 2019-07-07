##########################################################################
# Name:     Users
# Purpose: File contains Users
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from main import *
from tools import dbfill


def init_db():
    db.create_all()
    dbfill.fill_castes()
    dbfill.fill_districts()
    dbfill.fill_institutions()
    dbfill.fill_religions()
    dbfill.fill_roles()
    dbfill.fill_standards()
    dbfill.fill_states()
    dbfill.fill_subjects()
    dbfill.fill_towns()
    # dbfill.fill_user_roles()
    dbfill.fill_users()


application = create_app()
# with application.app_context():
#     init_db()


if __name__ == "__main__":
    application.run(debug=True, port=5000)
