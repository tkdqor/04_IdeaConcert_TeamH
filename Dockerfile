FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /srv/docker-server
ADD . /srv/docker-server

WORKDIR /srv/docker-server

COPY ./Pipfile /srv/docker-server/Pipfile
COPY ./Pipfile.lock /srv/docker-server/Pipfile.lock

RUN pip install pipenv
RUN pipenv install
RUN pipenv install uwsgi

EXPOSE 8000
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]