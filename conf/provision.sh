#!/usr/bin/env bash

sudo timedatectl set-timezone Europe/Warsaw
sudo locale-gen pl_PL.UTF-8

sudo apt-get update
sudo apt-get install -y python3-pip postgresql libpq-dev

cd /vagrant
sudo pip3 install -r conf/requirements.txt

sudo -u postgres psql -c "CREATE ROLE blue_user PASSWORD 'blue_pass' SUPERUSER INHERIT CREATEDB CREATEROLE LOGIN;"
sudo -u postgres psql -c "CREATE DATABASE blue_database WITH OWNER = blue_user ENCODING = 'UTF8' TABLESPACE = pg_default TEMPLATE template0;"
sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/9.3/main/postgresql.conf
sudo sed -i "s|host    all             all             127.0.0.1/32            md5|host    all             all             0.0.0.0/0            md5|g" /etc/postgresql/9.3/main/pg_hba.conf

cd src
./manage.py migrate
./manage.py loaddata menu/fixtures/menus.json
./manage.py loaddata menu/fixtures/dishes.json
./manage.py loaddata project_blue/fixtures/users.json
