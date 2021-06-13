FROM ubuntu:18.04
RUN apt-get update && apt-get install python3-setuptools python3-dev python3-pip build-essential -y

WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

# add (the rest of) our code
COPY . /code/

ENTRYPOINT ["/bin/bash", "/code/docker-entrypoint.sh"]


