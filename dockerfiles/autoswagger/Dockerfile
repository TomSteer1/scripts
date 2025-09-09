FROM python

RUN apt update && \
    apt install -y git && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/intruder-io/autoswagger.git
WORKDIR /autoswagger
RUN pip install -r requirements.txt
RUN python autoswagger.py

ENTRYPOINT [ "python", "autoswagger.py" ]
CMD [ "--help" ]