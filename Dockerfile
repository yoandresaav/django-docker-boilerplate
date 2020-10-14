FROM python:3.8-alpine
LABEL MAINTAINER="yoandre.saavedra@gmail.com"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client

RUN apk add --update --no-cache --virtual .tmp-buils-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt

RUN apk del .tmp-buils-deps

RUN mkdir /app
WORKDIR /app

COPY ./app /app

RUN adduser -D django
USER django