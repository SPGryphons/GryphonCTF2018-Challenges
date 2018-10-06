# SmashBros

## Question Text

Enabling no execute and ASLR should help me survive BOFs right?

`nc pwn.chal.gryphonctf.com 18401`

*Creator - PotatoDrug*

## Setup Guide
1. Enable ASLR
2. Run `./build.sh`

## Distribution
- smashbros
    - SHA1: `33eab43a50684dafe3430c43347b5988c98b1e17`
    - binary
- smashbros.c
    - SHA1: `d99470208566ddd015bf2c25297492140bba78c6`
    - source code
- libc-2.27.so
    - SHA1: `e3d54f5709190f15a9c51089c70f2069771913c1`

## Solution

If we take a look at the source code of `vuln` function it is obviously vulnerable to buffer overflow because it is using `gets`.
```c
void vuln(){
    char buf[32];
    printf("> ");
    gets(buf);
    printf("Bye\n");
}
```

Since the binary compiled with a non-executable stack, we cannot simply inject shellcode and jump to it. Instead we have to use a technique called return to libc.

The following prints the address of the LIBC object `_IO_2_1_stdin_`
```c
    printf("Here is your leaked LIBC address\nstdin: %p\n", stdin);
```

We find the offsets of `_IO_2_1_stdin_`, `system` and the string `/bin/sh` in the libc shared object used by the server
```bash
> readelf -s distrib/libc-2.27.so | grep "_IO_2_1_stdin_"
   400: 001d85c0   152 OBJECT  GLOBAL DEFAULT   34 _IO_2_1_stdin_@@GLIBC_2.1

> readelf -s distrib/libc-2.27.so | grep "system"
   254: 00129640   102 FUNC    GLOBAL DEFAULT   13 svcerr_systemerr@@GLIBC_2.0
   652: 0003d200    55 FUNC    GLOBAL DEFAULT   13 __libc_system@@GLIBC_PRIVATE
  1510: 0003d200    55 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.0

> strings -a -t x distrib/libc-2.27.so | grep "/bin/sh"
 17e0cf /bin/sh
```

Using offset of `stdin` and the leaked address of `stdin` we can calculate libc's base address using `leaked stdin address` - `stdin offset`.

We can then calculate the address of `system` function and `/bin/sh` string by adding their offset to the libc base address.

Now we are ready to make use of our buffer overflow. We use the overflow to overwrite the return address of the function with the address of `system` and give the address of the string `/bin/sh` as argument to give us a shell.

[Sample solution](solution/solve.py)

### Flag
`GCTF{huH_WH47_1s_4slR_4nd_nx}`
