# Math Test

## Question Text

The challenge title says it all :)

*Creator - Noans*

### Hints (Optional)
1. This ain't conventional math.

## Setup Guide
1. Run `./build.sh` in the service folder.

## Solution
Upon connecting to the service using telnet or netcat, one can start solving the math problem sums. Except, it will eventually be discovered that it isn't as simple simply running the `eval` function in python upon receiving the string.

The service program does not follow the conventional PEMDAS order of operations. One will need to figure out the order of operation used, and program a script to solve the challenge. Especially since only 3 seconds is given for each question.

Suggested Solution: [solution.go](../solution/solution.go)

### Flag
`GCTF{G00D_4T_M47H}`