FROM python:3.12-slim

RUN apt-get update -y
RUN apt-get install apt-transport-https ca-certificates gnupg curl git -y

RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" >> /etc/apt/sources.list.d/google-cloud-sdk.list

RUN apt-get update -y &&  apt-get install google-cloud-cli -y

WORKDIR /usr/src/

RUN git clone https://github.com/NetSPI/gcpwn.git
WORKDIR /usr/src/gcpwn
RUN chmod +x setup.sh
RUN ./setup.sh

RUN rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/bin/bash" ,"-c" ,"python3 /usr/src/gcpwn/main.py"]
