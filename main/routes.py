##########################################################################
# Name:     main Routes
# Purpose: File contains endpoints for index, home, and about requests
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import jsonify
from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
@main.route('/index')
def index():
    """
    default pages
    :return: Hello World
    """
    return jsonify({'message': 'Hello, World!'})
