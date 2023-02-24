#!/bin/bash
# Install wireshark and configure to capture as non-root user
# Peter Norris: 19 Sept 2018

# install wireshark (may already be there)
echo "During wireshark install, select \"Allow non-root users to capture traffic\" if offered." 1>&2
echo "sudo privilege is needed at several points in the script." 1>&2
echo "If you are unsure about granting sudo, then read the script first." 1>&2
sudo apt-get update && sudo apt-get install wireshark

# only proceed if wireshark group exists and dumpcap executable is on the $PATH
if grep -q wireshark /etc/group && which dumpcap > /dev/null
then
          # add the current user to the wireshark group
          sudo usermod -aG wireshark $USER

          # give member of wireshark group priv to capture traffic. Remove priv from others.
          DUMPCAP=$(which dumpcap)
          sudo chgrp wireshark $DUMPCAP
          sudo chmod o-rx $DUMPCAP
          sudo setcap 'cap_net_raw,cap_net_admin+eip' $DUMPCAP
else
          echo "Missing wireshark group and / or dumpcap executable. Aborting" 1>&2
          exit -1
fi

# confirm all is good
grep $USER /etc/group 1>&2
getcap $DUMPCAP 1>&2
