FROM python:3.6-alpine

# MAINTAINER INDIVISUAL APP DEVELOPER

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D newbert
USER newbert
