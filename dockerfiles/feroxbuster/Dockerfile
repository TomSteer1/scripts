FROM ubuntu

RUN apt update && apt install -y curl unzip git && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://raw.githubusercontent.com/epi052/feroxbuster/main/install-nix.sh | bash 

WORKDIR /usr/share
RUN git clone --depth 1 https://github.com/danielmiessler/SecLists.git seclists

ENTRYPOINT [ "/feroxbuster" ]