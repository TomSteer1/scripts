#!/bin/bash
# Install vmware drivers and sign key

git clone https://github.com/nan0desu/vmware-host-modules /tmp/vmware-host-modules
cd /tmp/vmware-host-modules

git checkout tmp/workstation-17.5.2-k6.9.1

make clean
make
sudo make install

filename_key="vmware_key"
sudo openssl req -new -x509 -newkey rsa:2048 -keyout ${filename_key}.priv -outform DER -out ${filename_key}.der -nodes -days 36500 -subj "/CN=VMware/"
sudo /usr/src/linux-headers-`uname -r`/scripts/sign-file sha256 ./${filename_key}.priv ./${filename_key}.der $(modinfo -n vmmon)
sudo /usr/src/linux-headers-`uname -r`/scripts/sign-file sha256 ./${filename_key}.priv ./${filename_key}.der $(modinfo -n vmnet)
sudo mokutil --import ${filename_key}.der 
echo "Now it's time for reboot, remember the password. You will get a blue screen after reboot choose 'Enroll MOK' -> 'Continue' -> 'Yes' -> 'enter password' -> 'OK' or 'REBOOT' "
