FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    bash \
    coreutils \
    binutils \
		findutils \
		file \
		binwalk \
		less \
    grep \
    sed \
    util-linux \
    neovim 


RUN echo 'alias vim="nvim"' >> /etc/bash.bashrc 
