#!/usr/bin/env python3
'''
Requires openssl
'''
import subprocess, sys

if len(sys.argv) != 2:
    print('Usage: {} <ciphertext>'.format(sys.argv[0]))
    exit()

for i in range(1,16385):
    binary = format(i, '014b')
    l = binary[:7] + '0'
    r = binary[7:] + '0'
    
    # skip if number of bits set is even
    if l.count("1") % 2 == 0 or r.count("1") % 2 == 0:
        continue
    
    candidate_key = format(int(l, 2), '02X') + '3D' + format(int(r, 2), '02X') + '021CEF32FB'
    process = subprocess.Popen(['openssl', 'enc', '-des-ecb', '-d', '-a', '-in', sys.argv[1], '-K',  candidate_key], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    
    if process.returncode == 0:
        try:
            print(out.decode("utf-8"))
        except:
            continue
        print("Key Found: {}".format(candidate_key))
        break
