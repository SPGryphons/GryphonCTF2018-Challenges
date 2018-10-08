#!/bin/sh
docker build -t typeracer .
docker run --restart always -d -p 18301:30152 --name prog-typeracer typeracer
docker start prog-typeracer
