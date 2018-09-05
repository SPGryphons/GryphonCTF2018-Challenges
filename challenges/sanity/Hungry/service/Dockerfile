FROM alpine

# standard stuff
RUN apk update \
    apk upgrade

# required packages & dependencies
RUN apk add python3 uwsgi
COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

# switch user
RUN adduser -D www-data
USER www-data
WORKDIR /home/www-data

# copy stuff in home dir
COPY sanity-hungry/ ./
WORKDIR /home/www-data/sanity-hungry

CMD ["uwsgi", "--socket", "0.0.0.0:5000", "--protocol=http", "-w", "wsgi:app"]
