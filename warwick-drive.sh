#!/usr/bin/env sh

sudo mount -t davfs -o rw,nosuid https://myfiles.warwick.ac.uk/hcwebdav/h-drive /mnt/h
sudo chown tom:tom /mnt/h
sudo chmod 770 /mnt/h

