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
00000000  07 03 14 06 7b 13 0f 5f  0d 01 0e 19 5f 17 01 19  |....{.._...._...|
00000010  13 5f 14 0f 5f 12 05 10  12 05 13 05 0e 14 5f 04  |._.._........._.|
00000020  01 14 01 7d                                       |...}|
00000024
```

Each byte in the file is a character, first byte is `0x07` which is `7` in decimal which is `G` after being decoded with A1Z26. We repeat the process for all bytes smaller than or equals to `0x1A` to get the flag.

[Sample solution](solution/solve.py)

### Flag
`GCTF{SO_MANY_WAYS_TO_REPRESENT_DATA}`
