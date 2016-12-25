#!/bin/sh

sudo service apache2 stop &
sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf &
sudo python3 /home/pi/IVMNM/manage.py runserver 0.0.0.0:80
