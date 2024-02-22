FROM mysql:latest

MAINTAINER Oscar McCabe

RUN chown -R mysql:root /var/lib/mysql

#ARG MYSQL_DATABASE
#ARG MYSQL_USER
#ARG MYSQL_PASSWORD
#ARG MYSQL_ROOT_PASSWORD

ENV MYSQL_DATABASE = ProgSocTest
ENV MYSQL_USER = ProgSoc
ENV MYSQL_PASSWORD = ProgSoc
ENV MYSQL_ROOT_PASSWORD = ProgSoc

#ADD init.sql /etc/mysql/data.sql

#RUN sed -i 's/MYSQL_DATABASE/'$MYSQL_DATABASE'/g' /etc/mysql/data.sql
#RUN cp /etc/mysql/data.sql /docker-entrypoint-initdb.d

#COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306

#ENTRYPOINT ["init"]
#RUN mysql /docker-entrypoint-initdb.d/init.sql
