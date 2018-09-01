# FlagData

## Question Text

This file contains data for a flag.

All the characters of the flag are uppercase.

*Creator - PotatoDrug*

## Distribution
- flag.dat
    - SHA1: `e46b87f131a9962fe216e991d8bed5c281122c2c`
    - Data file

## Solution
This is simplely A1Z26 cipher implemented with raw data. The following is the data in the file.

```
00000000: 0703 1406 7b13 0f5f 0d01 0e19 5f17 0119  ....{.._...._...
00000010: 135f 140f 5f12 0510 1205 1305 0e14 5f04  ._.._........._.
00000020: 0114 017d                                ...}
```

Each byte in the file is a character, first byte is `0x07` which is `7` in decimal which is `G` after being decoded with A1Z26. We repeat the process for all bytes smaller than or equals to `0x1A` to get the flag.

[Sample solution](solution/solve.py)

### Flag
`GCTF{SO_MANY_WAYS_TO_REPRESENT_DATA}`
