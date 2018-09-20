#!/bin/sh
docker build -t easybros .
docker run --restart always --memory 128M -dt -p 18000:5000 --name pwn-easybros easybros