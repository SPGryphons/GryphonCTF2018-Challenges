#!/bin/sh
docker build -t treasure .
docker run --restart always --memory 128M -d -p 18000:80 --name web-treasure treasure
