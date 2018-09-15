#!/usr/bin/env python3
from fractions import gcd

e = 65537
p = 4528450358010492026612439739120166758911246047493700040073956759261590397250033699357694507193523000343088601688589
q = 3968132623150957588532394439049887341769533966621957829426966084093049516953598120833228447171744337427374763106901
n = p*q

if gcd((p-1),e) != 1 or gcd((q-1),e) != 1:
    print('Error')
    exit()

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

plaintext = 'GCTF{r54_15_345Y_1F_Y0U_C4n_f4C70r_17}'

d = modinv(e, phi)
m = int.from_bytes(bytearray(plaintext, 'ascii'), byteorder='big', signed=False)
c = pow(m, e, n)

print('e = {}\nn = {}\nc = {}'.format(e,n,c))