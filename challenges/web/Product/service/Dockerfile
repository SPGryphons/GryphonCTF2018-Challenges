FROM tomcat:alpine

RUN rm -rf /usr/local/tomcat/webapps/*
COPY ./ROOT.war /usr/local/tomcat/webapps/

# create user
RUN adduser -DHs /sbin/nologin product

# fair warning - command takes some time to run
RUN chown -R product:product /usr/local/tomcat

USER product
CMD ["catalina.sh", "run"]
