FROM ubuntu:bionic

RUN apt-get update

RUN apt-get install -y python3-pip
RUN apt-get install -y redis-server
RUN apt-get install -y locales 

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . ./app
WORKDIR /app

ENV PYTHONIOENCODING=utf-8

RUN chmod +x ./run.sh
ENTRYPOINT ["./run.sh"]
