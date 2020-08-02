# Derived from official mysql image (our base image)
FROM mysql:latest
# Add a database

# Add the content of the sql-scripts/ directory to your image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup

ENV MYSQL_ROOT_PASSWORD 123 
ENV MYSQL_DATABASE twitter
ENV MYSQL_USER admin
ENV MYSQL_PASSWORD 1234
ADD docker-entrypoint-initdb.d
EXPOSE 3306