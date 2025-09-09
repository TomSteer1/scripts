FROM gcr.io/google.com/cloudsdktool/google-cloud-cli:stable

RUN apt update
RUN apt install -y curl
# RUN curl -sL https://firebase.tools | bash

# ENV CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE=SET_THIS
COPY setup.sh /setup.sh
RUN chmod +x /setup.sh

ENTRYPOINT [ "bash", "/setup.sh" ]