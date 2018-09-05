FROM alpine

# standard stuff
RUN apk update && \
    apk upgrade

# required packages & dependencies
RUN apk add python3 uwsgi uwsgi-python3
COPY requirements.txt ./
RUN python3 -m pip install -r requirements.txt

# add user
RUN adduser -s /sbin/nologin -D www-data

# permissions etc...
WORKDIR /var/www/html
COPY sanity-hungry/ /var/www/html/sanity-hungry
WORKDIR /var/www/html/sanity-hungry
RUN chown -R www-data:www-data .

CMD ["uwsgi", "--ini", "sanity-hungry.ini"]
