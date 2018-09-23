#!/usr/bin/env python3
import argparse, struct

parser = argparse.ArgumentParser(description='Encrypt a file')
parser.add_argument('-f','--file', help='Target file', required=True)
parser.add_argument('-o','--output', help='Output file', required=True)
parser.add_argument('-s','--seed', required=True)
parser.add_argument('-a','--multiplier', required=True)
parser.add_argument('-c','--increment', required=True)
args = vars(parser.parse_args())

def lcg(seed, a, c, p):
    last = (a * seed + c) % p
    while True:
        yield last
        last = (a * last + c) % p

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

with open(args['file'], 'rb') as f:
    content = bytearray(f.read())

s = int(args['seed'])
a = int(args['multiplier'])
c = int(args['increment'])
p = 2**32

prng = lcg(s,a,c,p)

while len(content) % 4 != 0:
    content.append(0)
content = [content[i:i+4] for i in range(0, len(content), 4)]

encrypted = bytearray()
for x in content:
    for y in struct.pack('>I', next(prng) ^ struct.unpack('>I', x)[0]):
        encrypted.append(y)

with open(args['output'], 'wb') as f:
    f.write(encrypted)

print('Encrypted {}'.format(args['file']))