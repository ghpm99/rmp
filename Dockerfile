# pull official base image
FROM python:3.9.7

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE rmp.settings.production

RUN mkdir /rmp

# set work directory
WORKDIR /rmp

# install dependencies
ADD requirements.txt /rmp/
RUN pip install -r requirements.txt

ADD . /rmp/

EXPOSE 8000