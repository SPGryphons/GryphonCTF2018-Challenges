#!/bin/sh
docker build -t knowingbros .
docker run --restart always --memory 128M -dt -p 18402:5000 --name pwn-knowingbros knowingbros
docker cp pwn-knowingbros:/lib/i386-linux-gnu/libc-2.27.so ../distrib/