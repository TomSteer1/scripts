#!/bin/bash

sudo apt update

# Install base packages
sudo apt install -y \
	git \
	curl \
	wget \
	pipx

pipx ensurepath

# Webwrap
curl -s https://raw.githubusercontent.com/mxrch/webwrap/master/install.sh | sudo sh

# gdb gef
sudo apt install -y \
	gdb \
	python3 \
	python3-pip \

bash -c "$(curl -fsSL https://gef.blah.cat/sh)"

# Install pwntools
pipx install pwntools

# Install radare2
sudo apt install -y radare2

# Install angr
pipx install angr

# Install z3
pipx install z3-solver

# Install rsaCtfTool
git clone https://github.com/RsaCtfTool/RsaCtfTool.git
sudo apt-get install libgmp3-dev libmpc-dev
cd RsaCtfTool
pip3 install -r "requirements.txt"
./RsaCtfTool.py
