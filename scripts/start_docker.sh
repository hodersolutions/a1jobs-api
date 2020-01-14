#!/bin/bash
/etc/init.d/nginx start
cd /home/www
gunicorn --bind 0.0.0.0:5000 run
