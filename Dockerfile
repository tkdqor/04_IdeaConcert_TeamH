FROM python: 3.9

ENV PYTHONUNBUFFERED 

RUN apt-get -y update

RUN mkdir /docker-server
ADD . /docker-server
WORKDIR /docker-server

RUN pip install pipevn
RUN pip pipenv install
RUN pipenv run python manage.py collectstatic