#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Decrypt a png file')
parser.add_argument('-f','--file', help='Target file', required=True)
parser.add_argument('-o','--output', help='Output file', required=True)
args = vars(parser.parse_args())

plaintext = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A\x00\x00\x00\x0D\x49\x48\x44\x52'
KEYLEN = len(plaintext)
key = []

with open(args['file'], 'rb') as f:
    content = bytearray(f.read())

# find key
for i in range(KEYLEN):
    key.append(content[i] ^ plaintext[i])

# decrypt file
for i in range(len(content)):
    content[i] ^= key[i % KEYLEN]

with open(args['output'], 'wb') as f:
    f.write(content)