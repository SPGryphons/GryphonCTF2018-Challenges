#!/usr/bin/env python3

with open('../distrib/flag.dat', 'rb') as f:
    content = f.read()

flag = ''
for b in content:
    if b > 26:
        flag += chr(b)
    else:
        flag += chr(b + 64)

print(flag)
