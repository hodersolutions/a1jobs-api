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


application = create_app()
# with application.app_context():
#     db.create_all()

if __name__ == "__main__":
    application.run(debug=True, port=5000)
