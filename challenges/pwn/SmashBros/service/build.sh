#!/bin/sh
docker build -t smashbros .
docker run --restart always --memory 128M -dt -p 18000:5000 --name pwn-smashbros smashbros
docker cp pwn-smashbros:/lib/i386-linux-gnu/libc-2.27.so ../distrib/
