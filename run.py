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

db.create_all()
from tools import dbfill
dbfill.fill_reservations()
dbfill.fill_states()
dbfill.fill_districts()
dbfill.fill_towns()
dbfill.fill_institutions()
dbfill.fill_religions()
dbfill.fill_subjects()
dbfill.fill_job_types()
dbfill.fill_qualifications()

if __name__ == "__main__":
	application.run(debug=True, port=5000)
