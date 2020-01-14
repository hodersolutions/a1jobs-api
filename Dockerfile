FROM pythonbase

RUN apt-get update && \
  apt-get install -y nginx gunicorn


RUN mkdir /home/www && cd /home/www
COPY . /home/www/
RUN pip3 install -r /home/www/requirements.txt
RUN /etc/init.d/nginx start
RUN rm /etc/nginx/sites-enabled/default
RUN cp /home/www/scripts/a1jobs-api /etc/nginx/sites-available/a1jobs-api
RUN ln -s /etc/nginx/sites-available/a1jobs-api /etc/nginx/sites-enabled/a1jobs-api
RUN ["chmod", "+x", "/home/www/scripts/start_docker.sh"]
CMD ["/home/www/scripts/start_docker.sh"]


# update pip



