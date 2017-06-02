

        FROM ubuntu:14.04

        RUN                 apt-get update -y &&                apt-get install python3-pip -y

        RUN     pip3 install mysql-connector==2.1.4

        RUN     mkdir -p /usr/src/app

        RUN     apt-get install mysql-server -y

        WORKDIR /usr/src/app

        COPY    . /usr/src/app

        CMD                 /etc/init.d/mysql start &&                /etc/init.d/mysql status &&                echo "create database c9" | mysql -u root &&                echo "SHOW DATABASES" | mysql -u root &&                cd src && python3 import.py



