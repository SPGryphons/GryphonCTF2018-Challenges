#!/bin/sh
docker build -t disguise .
docker run --restart always --memory 128M -d -p 18700:3000 --name web-disguise disguise
