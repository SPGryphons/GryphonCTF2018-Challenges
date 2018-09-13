#!/usr/bin/env sh
docker build --ulimit nofile=1024 -t rev-stolen .
docker run --security-opt seccomp=unconfined -dit -p 18000:8080 --name rev-stolen rev-stolen xinetd -d
