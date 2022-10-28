#!/usr/bin/env sh

sudo mount -t davfs -o rw,nosuid https://myfiles.warwick.ac.uk/hcwebdav/h-drive /mnt/h
sudo chown $(whoami):$(id -ng) /mnt/h
sudo chmod 770 /mnt/h

