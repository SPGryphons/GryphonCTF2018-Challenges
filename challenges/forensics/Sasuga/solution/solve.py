#!/usr/bin/env python3
import zlib, struct, argparse

parser = argparse.ArgumentParser(description='Fix a corrupted png file')
parser.add_argument('-f','--file', help='PNG file to be fixed', required=True)
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
def replaceBytes(data, offset, n, newData):
    bdataArray = struct.pack('!I', newData)
    for i in range(n):
        data[offset-(n-i)] = bdataArray[i]

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

def checkcrc(chunk_type_data, checksum):
    # CRC-32 computed over the chunk type and chunk data, but not the length
    calc_crc = struct.pack('!I', zlib.crc32(chunk_type_data) & 0xffffffff)
    if calc_crc != checksum:
        return calc_crc
    else:
        return None

# fix file header
replaceBytesArray(content, 8, 8, b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a')
# change lDAT back to IDAT
content = content.replace(b'lDAT', b'IDAT')

offset = -1
prev_offset = -1
count = 0
prev_offset = content.find(b'IDAT', 0)
while True:
    offset = content.find(b'IDAT', prev_offset+1)
    if offset == -1 or prev_offset == -1: break
    replaceBytes(content, prev_offset, 4, calcLength(prev_offset, offset))
    checksum = checkcrc(content[prev_offset:offset-8], content[offset-8:offset-4])
    if checksum != None:
        replaceBytesArray(content, offset-4, 4, checksum)
    prev_offset = offset
    count += 1

# last chunk
lastidatchunk = content.rfind(b'IDAT')
iendchunk = content.rfind(b'IEND')
replaceBytes(content, lastidatchunk, 4, calcLength(lastidatchunk, iendchunk))
checksum = checkcrc(content[lastidatchunk:iendchunk-8], content[iendchunk-8:iendchunk-4])
if checksum != None:
    replaceBytesArray(content, iendchunk-4, 4, checksum)
# tmp = length.to_bytes(4, byteorder='big', signed=False)
# content[offset-4] = tmp[0]
# content[offset-3] = tmp[1]
# content[offset-2] = tmp[2]
# content[offset-1] = tmp[3]

print('Fixed {} chunks'.format(count))

with open(args['output'], 'wb') as f:
    f.write(content)