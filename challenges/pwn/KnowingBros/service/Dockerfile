FROM i386/ubuntu:18.04

ENV USERNAME=knowingbros

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y xinetd

RUN useradd -s /usr/sbin/nologin -m ${USERNAME}

COPY ./flag /home/${USERNAME}/
COPY ./knowingbros.conf /etc/xinetd.d/knowingbros
COPY ./knowingbros /home/${USERNAME}/

RUN chown -R root:${USERNAME} /home/${USERNAME} && \
    chmod -R 750 /home/${USERNAME}

EXPOSE 5000
CMD ["/usr/sbin/xinetd", "-d"]