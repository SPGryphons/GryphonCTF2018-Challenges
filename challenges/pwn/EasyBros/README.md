# EasyBros

## Question Text

I turned off all protections just for you!

*Creator - PotatoDrug*

## Setup Guide
1. Run `./build.sh`

## Distribution
- easybros
    - SHA1: `2ac0a882dd6199198592e99f68d07432c60a16f9`
    - 32 bit ELF binary
- easybros.c
    - SHA1: `6ded52d35993bab6eeb1eb86d46c0eda49bc14ec`
    - source code

## Solution
`vuln` function is vulnerable to buffer overflow as it's using `gets`.
```c
void vuln(){
    char buf[128];
    printf("> ");
    gets(buf);
    printf("Bye\n");
}
```

If we run `checksec` we can see that all the protections are turned off.
```
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
```

Firstly you need to find the number of bytes required to overwrite the return address, in this case it is 140. Then get shellcode to give us a shell. And finish it off by overwriting the return address with an address pointing to anywhere in the nop slide.

`nop slide` + `shellcode` + `return address`

[Sample solution](solution/solve.py)

### Flag
`GCTF{1_C0uld_l4uncH_4_cyB3r_nUk3}`