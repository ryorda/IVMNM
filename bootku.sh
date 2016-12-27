#!/bin/bash
echo " ---- Begin IVMNM ----- "
echo " ---- Starting INIT SEQUENCE ----"
#/bin/mount --rw /dev/mmcblk0p2 /
#/bin/mount -t vfat /dev/mmcblk0p1 /boot
/bin/mount -t proc none /proc
/bin/mount -t sysfs none /sys
/etc/init.d/mountkernfs.sh start
/etc/init.d/mountall.sh start
#/etc/init.d/mountfs.sh start
#/etc/init.d/mountdevsubfs.sh start

/etc/init.d/fake-hwclock start
/etc/init.d/hostname.sh start
/etc/init.d/udev start
/etc/init.d/procps start
/etc/init.d/networking start # turn on network interfaces
# /etc/init.d/dh client start
/etc/init.d/hostapd start
# /etc/init.d/isc-dhcp-server start
#/sbin/sulogin
# /etc/init.d/dhcpcd start
sudo /etc/init.d/dnsmasq start
# /bin/login

echo " --- SETUP NETWORK LOGIN --- "

/home/pi/autorun.sh

