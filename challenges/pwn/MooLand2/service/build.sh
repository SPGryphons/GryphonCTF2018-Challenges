#!/bin/sh
docker build -t mooland2 .
docker run --restart always --memory 128M -d --cap-drop=all -p 18405:5000 --name pwn-mooland2 mooland2
docker start pwn-mooland2
