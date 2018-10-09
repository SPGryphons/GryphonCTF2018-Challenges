FROM ubuntu:latest

ENV USERNAME=validat0r

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y xinetd
RUN apt-get install -y libc6-i386

RUN useradd -s /usr/sbin/nologin -m ${USERNAME}

COPY ./validat0r.conf /etc/xinetd.d/validat0r
COPY ./exec.sh /home/${USERNAME}/
COPY ./validat0r /home/${USERNAME}/

RUN chown -R root:${USERNAME} /home/${USERNAME} && \
    chmod -R 750 /home/${USERNAME}

EXPOSE 8888
CMD ["xinetd", "-d"]