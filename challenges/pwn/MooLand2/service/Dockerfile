FROM node:9-alpine

RUN adduser -s /bin/rbash -D moo
RUN apk add --no-cache bash

RUN mkdir /home/moo/progs

COPY ./cowsay /home/moo/progs/

COPY ./banner.txt /home/moo/
COPY ./flag.txt /home/moo/
COPY ./server.js /home/moo/

RUN chown -R root:moo /home/moo && \
    chmod -R 750 /home/moo

USER moo
WORKDIR /home/moo
ENV HOME=/home/moo
ENV PATH=/home/moo/progs
EXPOSE 5000

CMD ["/usr/local/bin/node", "/home/moo/server.js"]