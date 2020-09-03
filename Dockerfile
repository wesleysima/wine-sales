FROM python:3.7-alpine
LABEL maintainer="wesley-sima@hotmail.com"

RUN apk add --no-cache nginx ca-certificates tzdata git openjdk8-jre \
	gcc linux-headers libffi-dev jpeg-dev build-base flex bison wget \
    zlib-dev mariadb-connector-c-dev nodejs npm cmake unzip \
    && mkdir /run/nginx

ENV LIBRARY_PATH=/lib:/usr/lib
ENV TZ=America/Sao_Paulo

COPY app /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install supervisor gunicorn Django==2.2.*
RUN pip install -r requirements.txt

COPY nginx.conf /etc/nginx/nginx.conf
COPY supervisord.conf /etc/supervisord.conf

CMD supervisord