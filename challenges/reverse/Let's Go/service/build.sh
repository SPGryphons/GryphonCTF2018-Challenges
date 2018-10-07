#!/bin/sh
docker build -t lets-go .
docker run --restart always --memory 128M -dt -p 80:8000 --name rev-lets-go lets-go