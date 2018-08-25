# Desparupto

## Question Text

I can't decrypt my DES-ECB encrypted flag because my key is corrupted!

Corrupted Key: `4E3D42021CEF32FB`

*Creator - PotatoDrug*

### Hints (Optional)
1. DES uses Odd Parity

## Distribution
- Desparupto
    - SHA1: `9161e90481ce2131a693a397345dca4fbe4819e8`
    - DES-ECB encrypted ciphertext

## Solution
DES has a 64 bit key, however the Least Significant Bit (LSB) of each byte is a parity bit. So we check the parity bits and find that the 1st and 3rd byte are corrupted.

We then have to bruteforce the 2 bytes to find the correct key, since the LSB of each byte is a parity bit we only have to deal with 2 x 7 bits instead of 2 x 8. We can also eliminate bytes with an even number of bits set since DES uses odd parity and the parity bit for both bytes are set to 0. So effctively our search space is only `(2**14)/2 = 8192`.

[Sample Solution](solution/solve.py)

Original key `CE3D46021CEF32FB`

### Flag
`GCTF{ParrI7y_8i7_S7Ill_US3fuL_oR_Nah}`

## Recommended Reads
* http://blog.listincomprehension.com/2010/10/setting-parity-on-des-keys.html
