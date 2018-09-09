# Forest

## Question Text

I am lost in a vast forest, find me!

*Creator - Noans*

## Setup Guide
1. Run the generate program.
2. Open a file `521` and change the contents to contain the flag.

## Distribution
- forest.zip
    - SHA1: `1753b54b9b11e9beb3044d8efbae47ec09dced63`
    - A zipped file containing 1000 files.

## Solution
Looking into the files after unzipping the distributed zip file, one will notice that they simply contain text starting with GCTF.

To solve the challenge, program a script as offered in the [solution](../solution/Solution.java). The output will show 10 files matching the regex. Using either a sensible guess, or trial-and-error, the right flag will eventually be found.

### Flag
`GCTF{E7R3M3LY_H4RD_T0_F1ND_7H15_N3EDL3}`
