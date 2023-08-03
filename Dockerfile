FROM python:3.9.15

RUN sed -i s/deb.debian.org\\/debian\ stretch-updates/archive.debian.org\\/debian\ stretch/g /etc/apt/sources.list
RUN sed -i s/deb.debian.org\\/debian\ stretch/archive.debian.org\\/debian\ stretch/g /etc/apt/sources.list
RUN sed -i s/security.debian.org\\/debian-security\ stretch/archive.debian.org\\/debian-security\ stretch/g /etc/apt/sources.list

RUN apt-get update \
&& apt-get install -y postgresql postgresql-contrib libpq-dev python3-dev

RUN pip3 install --upgrade pip

COPY ./Blog ./
COPY requirements.txt ./Blog/requirements.txt
RUN pip3 install -r ./Blog/requirements.txt

COPY ./wait-for-postgres.sh .
RUN chmod +x ./wait-for-postgres.sh

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1