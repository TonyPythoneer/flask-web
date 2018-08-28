FROM python:3.7-slim

WORKDIR /app

ADD . /app

CMD tail -f /dev/null
