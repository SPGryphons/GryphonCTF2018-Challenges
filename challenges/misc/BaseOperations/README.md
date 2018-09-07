# BaseOperations

## Question Text

So many bases...

*Creator - PotatoDrug*

### Hints (Optional)
1. Each encoding uses a smaller base.

## Distribution
- BaseOperations.txt
    - SHA1: `d867141a2f14ed6bd248b88aba52f3065efced3c`

## Solution
The flag is encoded `Base16 > Base32 > Base58 > Base64 > Base85` so to decode it we will do the reverse.

[CyberChef](https://gchq.github.io/CyberChef/) recipe
```
From_Base85('!-u')
From_Base64('A-Za-z0-9+/=',false)
From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',false)
From_Base32('A-Z2-7=',false)
From_Hex('Auto')
```

### Flag
`GCTF{MUcH_3ncoDIn9_V3RY_AmA2In9}`
