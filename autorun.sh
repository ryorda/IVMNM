#!/bin/sh

sudo service apache2 stop
#WLAN_STATS=$(sudo /etc/init.d/dhcpcd status | grep "Active: active")
#echo "W: _$WLAN_STATS_"
#while [ -z "$WLAN_STATS" ]; do
#	echo "waiting for dhcpcd setup..."
#	sleep 1
#	WLAN_STATS=$(sudo /etc/init.d/dhcpcd status | grep "Active: active");	
#done

#WLAN_STATS=$(sudo /etc/init.d/hostapd status | grep "Active: active")
#echo "W: _$WLAN_STATS_"
#while [ -z "$WLAN_STATS" ]; do
#	echo "waiting for hostapd setup..."
#	sleep 1
#	WLAN_STATS=$(sudo /etc/init.d/hostapd status | grep "Active: active");	
#done

#sudo /etc/init.d/networking status
#sudo /etc/init.d/dhcpcd status
#sudo /etc/init.d/hostapd status

sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf &
sleep 2
sudo /usr/sbin/hostapd /etc/hostapd/hostapd.conf &
echo "5" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio5/direction
echo "1" > /sys/class/gpio/gpio5/value
sudo python3 /home/pi/IVMNM/manage.py runserver 0.0.0.0:80
