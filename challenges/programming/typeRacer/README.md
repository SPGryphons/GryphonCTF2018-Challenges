# TypeRacer

## Question Text

They call me the fastest hand in the West.

`nc prog.chal.gryphonctf.com 18301`

*Creator - WhiteLight*

### Hints (Optional)
1. Hmmmmmmm why and how is the words in coloured?

## Setup Guide
Run `./build.sh`

## Solution

Since the challenge requires you to type 300 words in 1 minute which is impossible, you will need to write a script to echo back whatever you receive from the server.
However, take note that the words are coloured using ANSI escape code. 
Thus simple echoing back of the received string will not work. You will need to slice the string to remove the escape code before echoing back the string to the server.
`python3 solution.py | grep "GCTF{"`

### Flag
`GCTF{F457_F1N93R}`
