#!/bin/sh
docker build -t typeracer .
docker run --restart always -d -p 30152:30152 --name sanity-typeracer typeracer
docker start sanity-typeracer
