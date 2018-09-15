#!/usr/bin/env python3
import argparse
from os import urandom

parser = argparse.ArgumentParser(description='Encrypt a file')
parser.add_argument('-f','--file', help='Target file', required=True)
parser.add_argument('-o','--output', help='Output file', required=True)
args = vars(parser.parse_args())

KEYLEN = 16
key = urandom(KEYLEN)

with open(args['file'], 'rb') as f:
    content = bytearray(f.read())

for i in range(len(content)):
    content[i] ^= key[i % KEYLEN]

with open(args['output'], 'wb') as f:
    f.write(content)