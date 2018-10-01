#!/bin/sh
docker build -t falkreath .
docker run --restart always --memory 128M -dt -p 18403:5000 --name pwn-falkreath falkreath