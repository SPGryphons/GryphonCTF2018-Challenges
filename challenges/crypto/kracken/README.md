# Kracken

## Question Text

The Kracken is growing restless

*Creator - Noans*

### Hints (Optional)
1. It's a known plaintext attack

## Distribution
- kraken.zip
    - SHA1: `6fce079efb841c12a0d16076f5bcdee4fe0eabc5`

## Solution
The file is zip using the classic Linux `zip` utility. It is vulnerable to a known plaintext attack known as `pkcrack`.

Download the `https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack/pkcrack-1.2.2.tar.gz` and compile it using make. Use the `pkcrack` binary to crack with the correct commands.

[solution](solution/solution.sh)

### Flag
`GCTF{KR4CK3N_UNL345H3D}`
