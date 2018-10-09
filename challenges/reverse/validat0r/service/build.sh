#!/bin/sh
docker build -t validat0r .
docker run --restart always -dit -p 18503:8888 --name rev-validat0r validat0r