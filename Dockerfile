FROM python:3.6


WORKDIR /code

COPY requirements.txt /code/
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt

# add (the rest of) our code
COPY . /code/

ENTRYPOINT ["/bin/bash", "/code/docker-entrypoint.sh"]


