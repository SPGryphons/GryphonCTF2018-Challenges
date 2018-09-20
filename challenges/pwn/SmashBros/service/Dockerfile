FROM i386/ubuntu:18.04

ENV USERNAME=smashbros

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get update && apt-get install -y xinetd

RUN useradd -s /usr/sbin/nologin -m ${USERNAME}

COPY ./flag /home/${USERNAME}/
COPY ./smashbros.conf /etc/xinetd.d/smashbros
COPY ./smashbros /home/${USERNAME}/

RUN chown -R root:${USERNAME} /home/${USERNAME} && \
    chmod -R 750 /home/${USERNAME}

EXPOSE 5000

CMD ["/usr/sbin/xinetd", "-d"]