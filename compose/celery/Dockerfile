FROM ubuntu:18.04

ARG UNAME=celeryuser
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-distutils


RUN apt-get install -y \
    git \
    cmake \
    autoconf \
    autotools-dev \
    vim \
    wget \
    tar \
    firefox

RUN echo "y" | apt install python-psycopg2
RUN echo "y" | apt install libpq-dev python-dev
RUN echo "y" | apt install npm
RUN npm install -g loadtest

COPY ./requirements.txt /scripts/
RUN pip3 install --no-cache-dir -r /scripts/requirements.txt

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
RUN tar -xvzf geckodriver*
RUN chmod +x geckodriver
RUN mv geckodriver /usr/local/bin/
RUN echo "y" | apt install xvfb

COPY ./script.sh /scripts/
ENV DISPLAY=:0

WORKDIR /src/
USER $UNAME