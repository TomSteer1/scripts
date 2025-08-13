FROM python

RUN apt-get update && apt-get install -y \
    build-essential \
    neovim \
    git \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN echo "alias vim='nvim'" >> /root/.bashrc

ENTRYPOINT [ "/bin/bash" ]