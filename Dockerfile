FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000
