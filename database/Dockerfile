FROM mysql:latest

ENV MYSQL_DATABASE=ProgSocTest
ENV MYSQL_USER=ProgSoc
ENV MYSQL_PASSWORD=ProgSoc
ENV MYSQL_ROOT_PASSWORD=ProgSoc

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
