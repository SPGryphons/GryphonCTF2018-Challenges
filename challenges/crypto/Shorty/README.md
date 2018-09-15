# Shorty

## Question Text

Nothing good happens when your key length is too short, especially for XOR...

*Creator - PotatoDrug*

### Hints (Optional)
1. The key is 16 bytes

## Distribution
- Shorty.png
    - SHA1: `6cf4d12d1af5977341f8e91a28031134a2236b8f`
    - Encrypted png file

## Solution

The first 16 bytes of all png files are
```
00000000  89 50 4e 47 0d 0a 1a 0a  00 00 00 0d 49 48 44 52  |.PNG........IHDR|
```

Using this we can recover the 16 byte key used to encrypt the file. Since `Ciphertext ^ Plaintext = Key`. We can then use that key to decrypt the file.

[Sample solution](solution/solve.py)

### Flag
`GCTF{LOn93r_i5_83773rrRrRRRR}`