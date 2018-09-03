FROM python:3.7-slim

RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y build-essential python-dev

WORKDIR /app

COPY . /app
