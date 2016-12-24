#!/bin/sh

sudo service apache2 stop &
sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf &
sudo python3 manage.py runserver 0.0.0.0:80
