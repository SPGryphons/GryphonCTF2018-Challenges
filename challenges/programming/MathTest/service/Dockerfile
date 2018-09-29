FROM golang:1.11.0-alpine

RUN adduser -Ds /usr/sbin/nologin mathtest
WORKDIR /home/mathtest
COPY server.go .
RUN chown -R mathtest:mathtest .

USER mathtest
CMD ["go", "run", "server.go"]