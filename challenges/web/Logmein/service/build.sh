#!/bin/sh
docker build -t logmein .
docker run --restart always --memory 128M -d -p 18703:3000 --name web-logmein logmein