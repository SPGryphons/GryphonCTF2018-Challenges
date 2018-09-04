#!/usr/bin/env python3

with open('../distrib/Order', 'rb') as inf:
    with open('reversed.jpg', 'wb') as outf:
        outf.write(inf.read()[::-1])
