FROM python:

ENV PYTHONUNBUFFERED 1

WORKDIR /APP

ADD . /APP

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8000
