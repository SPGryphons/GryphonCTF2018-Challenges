#!/bin/sh
docker build -t san-netcat .
docker run --restart always --memory 128M -d -p 18600:5000 --name san-netcat san-netcat
