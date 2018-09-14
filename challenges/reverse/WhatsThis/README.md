# What's This

## Question Text

My flag's gotta be somewhere here.

*Creator - Noans*

## Distribution
- WhatsThis
    - SHA1: `da744a4fe5d9ad3662a95715433a5205f96fabbb`
    - A program written in C

## Solution
For this challenge, it is pretty simple to obtain the flag.

The file provided is a C program. Since the flag is allocated directly as a variable in the program, running `strings WhatsThis` will help attain the flag.

### Flag
`GCTF{7H15_W45_EZ}`
