# Cosmos

## Question Text

What's in the Cosmos?

*Creator - PotatoDrug*

### Hint
There are some suspicious spaces near the middle of the file

## Setup Guide
1. Run `generate/generate.py -f generate/bd_ch1.txt -o distrib/Cosmos.txt -t 'GCTF{kO5MO5_15_4_F4NCy_Word}' -s 500`

## Distribution
- Cosmos.txt
    - SHA1: `4dd0a33d7a5b081ac610d8aebff5ffec6eb15935`

## Solution
The flag is hidden in the spaces of the text file around the middle of the text file, Non-breaking spaces represent a 1 and normal spaces represent a 0. Using that we can extract out binary information and convert it to ascii to get out flag.

Also an important thing to note is 7 bit ascii is being used.

[Sample Solution](solution/solve.py)

### Flag
`GCTF{kO5MO5_15_4_F4NCy_Word}`
