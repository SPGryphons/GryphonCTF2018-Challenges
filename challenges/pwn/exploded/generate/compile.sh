#!/usr/bin/env sh
cc -fno-stack-protector -o test test.c
cc -fno-stack-protector -o service service.c
cp test ../distrib/exploded
cp service ../service/exploded
