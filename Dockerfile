# Derived from official mysql image (our base image)
FROM mysql:latest
# Add a database
FROM jupyter/scipy-notebook

FROM python:3.8-alpine

FROM continuumio/anaconda3:4.4.0

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup

COPY . /usr/app/


EXPOSE 5000

WORKDIR /usr/app/

RUN pip install -r requirements.txt



# ENV MYSQL_ROOT_PASSWORD 123 
# ENV MYSQL_DATABASE twitter
# ENV MYSQL_USER admin
# ENV MYSQL_PASSWORD 1234

# EXPOSE 3306

