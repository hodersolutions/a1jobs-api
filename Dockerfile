FROM pythonbase

RUN apt-get update && \
  apt-get install -y nginx gunicorn


RUN mkdir /home/www && cd /home/www
COPY . /home/www/
RUN pip3 install -r /home/www/requirements.txt
RUN /etc/init.d/nginx start
RUN rm /etc/nginx/sites-enabled/default
RUN cp /home/www/scripts/vanvia-api /etc/nginx/sites-available/vanvia-api
RUN ln -s /etc/nginx/sites-available/vanvia-api /etc/nginx/sites-enabled/vanvia-api
RUN ["chmod", "+x", "/home/www/scripts/start_docker.sh"]
CMD ["/home/www/scripts/start_docker.sh"]


# update pip



