FROM debian:9

ENV PYTHONUNBUFFERED=True

RUN sed -i 's#deb.debian.org#ba.mirror.garr.it/mirrors#g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-setuptools
RUN apt-get install -y ca-certificates
RUN easy_install3 pip

ADD requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt

ARG SERVICE_PORT
ENV SERVICE_PORT=${SERVICE_PORT}
EXPOSE ${SERVICE_PORT}

ENTRYPOINT python3 /opt/app.py
ADD app.py /opt/
