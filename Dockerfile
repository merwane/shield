FROM ubuntu:bionic

RUN apt-get update

RUN apt-get install -y python3-pip
RUN apt-get install -y redis-server
RUN apt-get install -y locales
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev cargo
RUN apt-get install -y ffmpeg libsm6 libxext6

COPY requirements.txt /
RUN pip3 install setuptools_rust
RUN pip3 install --no-cache-dir Cython
RUN pip3 install numpy
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

COPY . ./app
WORKDIR /app

ENV PYTHONIOENCODING=utf-8

RUN chmod +x ./run.sh
ENTRYPOINT ["./run.sh"]