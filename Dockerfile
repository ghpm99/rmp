FROM python:3.9.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /rmp
WORKDIR /rmp
ADD requirements.txt /rmp/
RUN pip install -r requirements.txt
ADD . /rmp/
EXPOSE 8000