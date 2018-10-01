FROM ubuntu:latest

ENV USERNAME=falkreath

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y xinetd

RUN useradd -s /usr/sbin/nologin -m ${USERNAME}

COPY ./exec.sh /home/${USERNAME}/
COPY ./Falkreath.conf /etc/xinetd.d/Falkreath
COPY ./Falkreath /home/${USERNAME}/

RUN chown -R root:${USERNAME} /home/${USERNAME} && \
    chmod -R 750 /home/${USERNAME}

EXPOSE 5000

CMD ["/usr/sbin/xinetd", "-d"]