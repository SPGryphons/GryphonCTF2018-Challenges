#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Extract data from a text file')
parser.add_argument('-f','--file', help='Carrier file', required=True)
args = vars(parser.parse_args())

NBS = '\u00A0'
secretbits = ''

with open(args['file'], 'r') as f:
    content = f.read()

# retrieve bits
for i in range(len(content)):
    if content[i] == ' ':
        secretbits += '0'
    elif content[i] == NBS:
        secretbits += '1'

# add padding
while len(secretbits) % 7 != 0:
    secretbits += '0'

n = 7
# split to list of 7 bits
secretbits = [secretbits[i:i+n] for i in range(0, len(secretbits), n)]
# remove null bytes
secretbits = list(filter(lambda a: a != '0000000', secretbits))

# parse bits
for c in secretbits:
    print(chr(int(c, 2)), end='')
print()