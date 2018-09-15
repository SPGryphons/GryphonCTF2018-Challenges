FROM tomcat:alpine

COPY ./ROOT /usr/local/tomcat/webapps/ROOT

# create user
RUN adduser -DHs /sbin/nologin myname
RUN chown -R myname:myname /usr/local/tomcat

USER myname
CMD ["catalina.sh", "run"]
