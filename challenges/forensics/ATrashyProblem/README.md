# A Trashy Problem

## Question Text
So I just found the photo of this bin. It's a very nice bin don't you think?

*Creator - whoami*

## Hint
I found a pillow in the bin too

## Distrib
* trash.png

## Solution
* solve.py
* Use a python script with Pillow to get the RGB values of each pixel and if the pixel has a value of (0,0,128), give it a binary value of 0 and if it has a value
of (128,0,0), give it a binary value of 1, then convert the binary values to ASCII text to get the flag

## Flag
`GCTF{P1X3LS_MAK3_M3_H3PPI3S}`
