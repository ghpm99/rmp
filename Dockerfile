# pull official base image
FROM python:3.9.7

# set work directory
WORKDIR /rmp

# set environment variables
ENV PYTHONUNBUFFERED 1


RUN mkdir /rmp
# install dependencies
ADD requirements.txt /rmp/
RUN pip install -r requirements.txt

ADD . /rmp/
ADD ./.profile.d /app/.profile.d

RUN python manage.py migrate --noinput

EXPOSE 8000