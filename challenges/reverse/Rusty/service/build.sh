#!/bin/sh
docker build -t rusty .
docker run --restart always --memory 128M -dt -p 18000:5000 --name rev-rusty rusty