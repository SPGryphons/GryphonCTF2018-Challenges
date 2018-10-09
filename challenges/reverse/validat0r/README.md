# validat0r

## Question Text

A program to check your password, if you have the same as mine, you get the flag :O

*Creator - @exetr (Chuan Kai)*

### Hints
1. Hint

## Setup Guide

Run `./build.sh`

## Distribution
- validat0r-distrib
    - SHA1: `3f356ed91d16a688fef1af0d3d2fc6dcdcafeb25`

## Solution

Since the password is stored as a char array, using `strings` on the compiled binary will not provide a direct answer to the challenge.

To get the "correct password", disassemble the binary and view the ASM source code

```
000006ad <validat0r>:
...
 6cd:	c7 85 7f ff ff ff 37 	movl   $0x35316837,-0x81(%ebp)
 6d4:	68 31 35 
 6d7:	c7 45 83 69 35 61 76 	movl   $0x76613569,-0x7d(%ebp)
 6de:	c7 45 87 33 72 79 5f 	movl   $0x5f77h15i5av3ry_v3ry_v3ry_v3ry_l0ng_p4ssw0rd_1otru0H125397233,-0x79(%ebp)
 6e5:	c7 45 8b 76 33 72 79 	movl   $0x79723376,-0x75(%ebp)
 6ec:	c7 45 8f 5f 76 33 72 	movl   $0x7233765f,-0x71(%ebp)
 6f3:	c7 45 93 79 5f 76 33 	movl   $0x33765f79,-0x6d(%ebp)
 6fa:	c7 45 97 72 79 5f 6c 	movl   $0x6c5f7972,-0x69(%ebp)
 701:	c7 45 9b 30 6e 67 5f 	movl   $0x5f676e30,-0x65(%ebp)
 708:	c7 45 9f 70 34 73 73 	movl   $0x73733470,-0x61(%ebp)
 70f:	c7 45 a3 77 30 72 64 	movl   $0x64723077,-0x5d(%ebp)
 716:	c7 45 a7 5f 31 6f 74 	movl   $0x746f315f,-0x59(%ebp)
 71d:	c7 45 ab 72 75 30 48 	movl   $0x48307572,-0x55(%ebp)
 724:	c7 45 af 31 32 35 33 	movl   $0x33353231,-0x51(%ebp)
```

Keep in mind that this is in little endian order, extracting the information in the ASM code, you can get

```
0x37683135
0x69356176
0x3372795f
0x76337279
0x5f763372 
0x795f7633 
0x72795f6c
0x306e675f 
0x70347373
0x77307264
0x5f316f74
0x72753048
0x31323533
```

which is `7h15i5av3ry_v3ry_v3ry_v3ry_l0ng_p4ssw0rd_1otru0H1253`

and 

```
~$ nc rev.chal.gryphonctf.com 18503
 _  _____ _/ (_)__/ /__ _/ /_/ _ \____
| |/ / _ `/ / / _  / _ `/ __/ // / __/
|___/\_,_/_/_/\_,_/\_,_/\__/\___/_/
                                    v1
--------------------------------------
password pls > 7h15i5av3ry_v3ry_v3ry_v3ry_l0ng_p4ssw0rd_1otru0H1253
GCTF{cann07_s7r1ng5_ch4r_4rr4y5}
```

### Flag
`GCTF{cann07_s7r1ng5_ch4r_4rr4y5}`