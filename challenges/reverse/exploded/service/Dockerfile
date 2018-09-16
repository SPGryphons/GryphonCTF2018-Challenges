FROM ubuntu
RUN apt update
RUN apt -y upgrade
RUN apt install -y xinetd

# add user & copy files
RUN useradd -ms /usr/sbin/nologin exploded
WORKDIR /home/exploded
COPY --chown=exploded:exploded flag .
COPY --chown=exploded:exploded exploded .
RUN chmod u+x exploded

# configure server
COPY exploded.conf /etc/xinetd.d/exploded
