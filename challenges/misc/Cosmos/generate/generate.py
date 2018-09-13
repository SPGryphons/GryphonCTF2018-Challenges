#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Hide data in a text file')
parser.add_argument('-f','--file', help='Carrier file', required=True)
parser.add_argument('-t','--text', help='Ascii text to be hidden', required=True)
parser.add_argument('-s','--skip', help='Number of bytes to skip', required=False)
parser.add_argument('-o','--output', help='output filename', required=True)
args = vars(parser.parse_args())

def replace_str_index(text,index,replacement):
    return '{}{}{}'.format(text[:index],replacement,text[index+1:])

NBS = '\u00A0'
secretbits = ''.join('{0:0{1}b}'.format(ord(x), 7) for x in args['text'])

with open(args['file'], 'r') as f:
    content = f.read()

skip = 7 * int(args['skip'])
count = 0
pos = -1
while True:
    pos = content.find(' ', pos+1)
    if pos == -1:
        print('Error: Carrier file does not contain enough spaces.')
        exit()
    count += 1
    if count == skip: break

for i in range(len(secretbits)):
    pos = content.find(' ', pos+1)
    if pos == -1:
        print('Error: Carrier file does not contain enough spaces.')
        exit()
    if secretbits[i] == '1':
        content = replace_str_index(content,pos,NBS)

with open(args['output'], 'w') as f:
    f.write(content)