#!/usr/bin/env python3
from os import urandom
import argparse

parser = argparse.ArgumentParser(description='Corrupt a png file')
parser.add_argument('-f','--file', help='PNG file to be corrupted', required=True)
parser.add_argument('-o','--output', help='output filename', required=True)
args = vars(parser.parse_args())

with open(args['file'], 'rb') as f:
  content = bytearray(f.read())

'''
Bytearray data
int offset (End index for replacement)
int n (number of bytes to replace)
int newData
'''
def replaceBytesArray(data, offset, n, newData):
    for i in range(n):
        data[offset-(n-i)] = newData[i]

def calcLength(offset1, offset2):
    # minus 4 bytes each for Chunk Type, CRC, Length
    return offset2 - offset1 - 12

offset = -1
prev_offset = -1
prev_offset = content.find(b'IDAT', 0)
while True:
    offset = content.find(b'IDAT', prev_offset+1)
    if offset == -1 or prev_offset == -1: break
    # corrupt chunk length
    replaceBytesArray(content, prev_offset, 4, urandom(4))
    # corrupt chunk crc
    replaceBytesArray(content, prev_offset + calcLength(prev_offset, offset) + 8, 4, urandom(4))
    prev_offset = offset

# last block
lastidatchunk = content.rfind(b'IDAT')
replaceBytesArray(content, lastidatchunk, 4, urandom(4))
replaceBytesArray(content, lastidatchunk + calcLength(lastidatchunk, content.rfind(b'IEND')) + 8, 4, urandom(4))

# replace IDAT with lDAT
content = content.replace(b'IDAT', b'lDAT')
# replace file header
replaceBytesArray(content, 8, 8, urandom(8))

with open(args['output'], 'wb') as f:
  f.write(content)