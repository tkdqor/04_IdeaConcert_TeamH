FROM python:3.9

RUN apt-get -y update

RUN mkdir /docker-server
ADD . /docker-server
WORKDIR /docker-server

RUN pip install pipenv
RUN pipenv install
RUN pipenv shell
RUN python manage.py collectstatic

# CMD ["pipenv", "run", "python", "manage.py", "collectstatic"]