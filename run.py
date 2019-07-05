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

if __name__ == "__main__":
    application = create_app()

    application.run(debug=True, port=5000)
