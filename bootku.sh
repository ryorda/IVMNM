#!/bin/bash
echo " ---- Begin IVMNM ----- "
echo " ---- Starting INIT SEQUENCE ----"
/etc/init.d/mountkernfs.sh start
/etc/init.d/mountall.sh start
/etc/init.d/fake-hwclock start
/etc/init.d/hostname.sh start
/etc/init.d/udev start
/bin/mount -t proc none /proc
/bin/mount -t sysfs none /sys
/etc/init.d/procps start
/etc/init.d/networking start # turn on network interfaces
/etc/init.d/dhclient start
/etc/init.d/hostapd start
/etc/init.d/isc-dhcp-server start
/sbin/sulogin

echo " --- SETUP NETWORK LOGIN --- "
/etc/init.d/isc-dhcp-server stop
/etc/init.d/hostapd stop
/etc/init.d/networking stop
/etc/init.d/fake-hwclock stop
/etc/init.d/halt stop
