# 2D Barcode

## Question Text

It's a barcode! It's in two dimensions! It's also broken!!!

*Creator - exetr (Chuan Kai)*

### Hints
1. https://en.wikipedia.org/wiki/QR_code#/media/File:QRCode-2-Structure.png
2. https://www.thonky.com/qr-code-tutorial/introduction

## Setup Guide
1. Distribute file in `distrib`

## Distribution
- 001110011100111.png
    - SHA1: `16205CC4871D5FE7A88C8BE2D15765F21C3D13C2`

## Solution
1. Add the three positioning markings and the single alignment markings as marked in blue

>![Step 1](solution/step1.png)

2. Add the timing pattern as marked in blue

>![Step 2](solution/step2.png)

3. Add in format information, which can be derived from the filename of the picture to be of high ECC level and mask pattern 2, as highlighted in blue

>![Step 3](solution/step3.png)

4. Since this QR code has a high level of Error Correction Coding, at this stage, the flag can already be obtained by scanning it in its current form

>![Step 4](solution/step4.png)

5. One can further recover the QR code by using Reed-Solomon error recovering techniques

>![Step 5](solution/complete.png)

### Flag
`GCTF{2d_r33d_s0l0m0n}`

## Recommended Reads
- https://en.wikipedia.org/wiki/QR_code
- https://www.thonky.com/qr-code-tutorial/format-version-information
- https://www.thonky.com/qr-code-tutorial/format-version-tables
- http://datagenetics.com/blog/november12013/index.html