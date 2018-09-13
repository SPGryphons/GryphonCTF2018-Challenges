FROM ubuntu
RUN apt update
RUN apt -y upgrade
RUN apt install -y xinetd

# add user & copy files
RUN useradd -ms /usr/sbin/nologin stolen
WORKDIR /home/stolen
COPY --chown=stolen:stolen flag .
COPY --chown=stolen:stolen stolen .
RUN chmod u+x stolen

# configure server
COPY 01-disable-aslr.conf /etc/sysctl.d/
COPY stolen.conf /etc/xinetd.d/stolen

