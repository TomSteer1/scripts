FROM alpine:3.20.3

RUN echo 'Installing packages for Nikto.'
RUN apk add --update --no-cache --virtual .build-deps \
     perl \
     perl-net-ssleay \
     git 

RUN echo 'Creating the nikto group.' \
  && addgroup nikto \
  && echo 'Creating the nikto user.' \
  && adduser -G nikto -g "Nikto user" -s /bin/sh -HD nikto

ENV  PATH=${PATH}:/opt/nikto

RUN echo 'Downloading and installing Nikto.' \
  && cd /opt \
  && git init nikto \
  && cd nikto \
  && git remote add origin https://github.com/sullo/nikto.git \
  && git config core.sparseCheckout true \
  && echo "program/" >> /opt/nikto/.git/info/sparse-checkout \
  && git pull --depth=1 origin master \
  && mv program/* /opt/nikto/ \
  && rm -rf /opt/nikto/.git \
  && echo 'Nikto installed.'

USER nikto
WORKDIR /opt/nikto

ENTRYPOINT ["nikto.pl"]
