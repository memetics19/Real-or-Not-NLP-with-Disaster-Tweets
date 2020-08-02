# Derived from official mysql image (our base image)
FROM mysql:latest
# Add a database
FROM jupyter/scipy-notebook

From python:3.8-alpine
# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup

COPY i.ipynb /notebooks/i.ipynb

ENV MYSQL_ROOT_PASSWORD 123 
ENV MYSQL_DATABASE twitter
ENV MYSQL_USER admin
ENV MYSQL_PASSWORD 1234

EXPOSE 3306

RUN conda install --quiet --yes \
   'mysqlclient'
   