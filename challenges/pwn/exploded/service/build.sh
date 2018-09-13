#!/usr/bin/env sh
docker build --ulimit nofile=2048 -t pwn-exploded .
docker run --security-opt seccomp=unconfined -dit -p 18000:8080 --name pwn-exploded pwn-exploded xinetd -d
