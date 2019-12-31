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




# with application.app_context():
# #     init_db()


if __name__ == "__main__":
    # application = create_app()
    db.create_all()
    from tools import dbfill
    dbfill.fill_reservations()
    dbfill.fill_districts()
    dbfill.fill_institutions()
    dbfill.fill_religions()
    dbfill.fill_states()
    dbfill.fill_subjects()
    dbfill.fill_towns()
    app.run(debug=True, port=5000)
