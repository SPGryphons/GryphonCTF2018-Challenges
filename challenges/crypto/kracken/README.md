# Kracken

## Question Text

The Kracken is growing restless

*Creator - Noans*

## Distribution
- kraken.zip
    - SHA1: `31ff0557953c181b6309c44e773bb69a066158ee`

## Solution
The file is zip using the classic Linux `zip` utility. It is vulnerable to a known plaintext attack known as `pkcrack`.

Download the `https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack/pkcrack-1.2.2.tar.gz` and compile it using make. Use the `pkcrack` binary to crack with the correct commands.

[solution](solution/solution.sh)

### Flag
`GCTF{KR4CK3N_UNL345H3D}`
