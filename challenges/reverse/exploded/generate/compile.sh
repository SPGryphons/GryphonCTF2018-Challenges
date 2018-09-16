#!/usr/bin/env sh
cc -fno-stack-protector -o ../distrib/exploded test.c
cc -fno-stack-protector -o ../service/exploded service.c
