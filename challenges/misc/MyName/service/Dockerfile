FROM tomcat:alpine

RUN rm -rf /usr/local/tomcat/webapps/*
COPY ./ROOT /usr/local/tomcat/webapps/ROOT

# create user
RUN adduser -DHs /sbin/nologin myname

# fair warning - command takes some time to run
RUN chown -R myname:myname /usr/local/tomcat

USER myname
CMD ["catalina.sh", "run"]
