#!/bin/sh
docker build -t letsgo .
docker run --restart always --memory 128M -dt -p 18502:5000 --name rev-letsgo letsgo