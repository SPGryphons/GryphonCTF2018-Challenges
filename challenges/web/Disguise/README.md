# Disguise

## Question Text

What's this amazing light?

`http://web.chal.gryphonctf.com:18700`

*Creator - PotatoDrug*

## Setup Guide
Run `./build.sh`

## Solution

To get the flag you are supposed to send a post request to index.html

```bash
curl -X POST http://localhost:3000/index.html
```

The tricky part about this challenge is a dynamic site is disguising as a static site.

### Flag
`GCTF{pr377y_L19h7_pR377Y_7R1cKy}`
