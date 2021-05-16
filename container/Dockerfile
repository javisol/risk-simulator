# syntax=docker/dockerfile:1
FROM arm32v7/python:3.8-slim-buster

RUN mkdir -p risk/container
RUN mkdir -p /risk/simulator
WORKDIR /risk/container

COPY container/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY container/. /risk/container
COPY simulator/. /risk/simulator

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
