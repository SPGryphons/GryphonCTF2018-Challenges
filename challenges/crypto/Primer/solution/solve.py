#!/usr/bin/env python3
from fractions import gcd

e = 65537
c = 9928661807722383398820979230758435588537138202455120644439973790890900720696808116440067157927041318933822725810085818657063240323701048719466385696993936990970552773045996562866193610801687931437246456210397942884802012524529532
p = 4528450358010492026612439739120166758911246047493700040073956759261590397250033699357694507193523000343088601688589
q = 3968132623150957588532394439049887341769533966621957829426966084093049516953598120833228447171744337427374763106901
n = p*q
phi = (p-1)*(q-1)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

def decimalToAscii(num):
    tmp = num.to_bytes((num.bit_length() + 7) // 8, 'big')
    return tmp.decode('ascii')

plaintext = 'GCTF{flag}'

d = modinv(e, phi)

try:
    print(decimalToAscii(pow(c, d, n)))
except Exception:
    print('Decryption failed')