FROM python:3

WORKDIR /key_secret_tracker

COPY ./requirements.txt /key_secret_tracker/

RUN pip3 install -r /key_secret_tracker/requirements.txt

COPY . .