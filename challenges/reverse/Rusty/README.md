# Rusty

## Question Text

I am quite rusty with this :(

*Creator - PotatoDrug*

### Hints (Optional)
1. Find the interesting function
2. Check the data section

## Setup Guide
1. Run `./build.sh`

## Distribution
- rusty
    - SHA1: `00e254c6289ba81c70ac5bd1b6cb54edbb74bd4c`
    - 64 Bit ELF

## Solution

When we run the program it asks us for the password, so we have to find out what is the correct password.
```bash
> ./distrib/rusty 
Password > asd
No flags for you!
```

Firstly we have to find the main function, if we list all functions and grep for main in radare2 find it.
```
:> afl~main
0x0000c8c0   60 2157 -> 1771 sym.rusty::main::h07d7fd320c0f5e4e
```

While looking through the main function we find this interesting bit.
![alt text][solution/disasm.png]

Important thing to note
> In Rust a ‘string’ is a sequence of Unicode scalar values encoded as a stream of UTF-8 bytes. All strings are guaranteed to be a valid encoding of UTF-8 sequences. Additionally, unlike some systems languages, strings are not null-terminated and can contain null bytes.

We see a string being loaded and passed to a function named `rot13`. Then there is a string comparision, so it is likely that our input is being compared to the rot13 of this string. 
Since strings are not null terminated, we dont know until where this string `zLfHcrefRPergEhfgcebtenzcnfFJbeQFLAGcouldn't interpret :` is terminated and passed to `rot13` function. So we rot13 the whole string and get `mYsUpersECretRustprogrampasSWorDSYNTpbhyqa'g vagrecerg :` we can see that it is highly likely `mYsUpersECretRustprogrampasSWorD` is our password.

If we enter it to the program we can see that it really is the password!
```
➜ nc localhost 18000
Password > mYsUpersECretRustprogrampasSWorD
Here's your flag: GCTF{1s_RuS7_7H3_LAN9Ua93_0f_7h3_FU7uR3}
```

### Flag
`GCTF{1s_RuS7_7H3_LAN9Ua93_0f_7h3_FU7uR3}`