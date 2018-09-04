# Order 

## Question Text

I cant seem to make sense of this file I recieved. Please help!

*Creator - PotatoDrug*

## Distribution
- Order
    - SHA1: `cd401947b1a6acb4fac1e2995c3f75078a5ca150`

## Solution

```
000016a0  32 21 1c 21 32 18 0d 0d  18 0c 0b 0c 09 09 09 01  |2!.!2...........|                            
000016b0  43 00 db ff 32 34 33 2e  3c 32 38 3d 39 27 1f 34  |C...243.<28=9'.4|                            
000016c0  34 34 31 30 2c 29 37 28  1c 1c 23 2c 22 20 27 2e  |4410,)7(..#," '.|                            
000016d0  24 20 1c 1c 1a 1d 1e 1f  1a 1d 14 0f 13 12 19 0c  |$ ..............|                            
000016e0  0b 0b 0c 0d 14 0c 0a 08  09 09 07 07 07 08 05 06  |................|
000016f0  07 06 06 08 00 43 00 db  ff d8 ff                 |.....C.....|
```
If you open the file with a hex editor and look at the last few bytes, you will be able to see `ff d8 ff` which is the jpg file header. So to get the flag you need to reverse the order of the bytes.

[Sample Solution](solution/solve.py)

### Flag
`GCTF{C4N_yOU_r34D_84cKW4rDz}`
