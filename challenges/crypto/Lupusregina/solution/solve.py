#!/usr/bin/env python3
import argparse, struct, gmpy2

parser = argparse.ArgumentParser(description='Decrypt a file')
parser.add_argument('-f','--file', help='Target file', required=True)
args = vars(parser.parse_args())

def asciiToDecimal(msg):
    return int.from_bytes(bytearray(msg, 'ascii'), byteorder='big', signed=False)

def find_c(states, p, a):
    c = (states[1] - a * states[0]) % p
    return c
 
def find_a(states, p):
    a = (states[2] - states[1]) * gmpy2.invert(states[1] - states[0], p) % p
    return a
 
def lcg(seed, a, c, p):
    last = seed
    while True:
        yield last
        last = (a * last + c) % p

p = 2**32
 
with open(args['file'], 'rb') as f:
    content = bytearray(f.read())

while len(content) % 4 != 0:
    content.append(0)
content = [content[i:i+4] for i in range(0, len(content), 4)]
 
plaintext = 'Dear Lupusregina,\n'
assert len(plaintext) >= 12, 'Not enough known plaintext!'

plaintext = [plaintext[i:i+4] for i in range(0, len(plaintext), 4)]

states = []
for i in range(3):
    states.append(asciiToDecimal(plaintext[i]) ^ struct.unpack('>I', content[i])[0])

s = states[0]
a = find_a(states, p)
c = find_c(states, p, a)

prng = lcg(s, a, c, p)

decrypted = bytearray()
for x in content:
    for y in struct.pack('>I', next(prng) ^ struct.unpack('>I', x)[0]):
        decrypted.append(y)

print(decrypted.decode("utf-8"))