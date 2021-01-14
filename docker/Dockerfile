FROM ubuntu:20.04
ENV TZ=Europe/Copenhagen
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Setup common system level packages
RUN apt-get update -y &&\
	apt-get install -y python-is-python3 python3-pip r-base gcc pipenv

COPY competition-analysis /analysis

COPY python3 /run
WORKDIR /run

RUN pipenv lock --requirements >> requirements.txt
RUN pip3 install -r requirements.txt

COPY python3/algorithms/* /run
