# Let's Go

## Question Text

Lets Go find the password!

(please encapulate the password in GCTF{...} to submit)
`nc rev.chal.gryphonctf.com 80`

*Creator - lohkaimun99*

### Hints (Optional)
1. salty salty md5

## Setup Guide
1. Distribute Lets-Go

## Distribution
- Let's Go
    - SHA1: `d224a274b6a2e40f79f13123c9b31b578a7255f0`
    - 64 Bit ELF

## Solution
The program will ask for the password, which it will compute the some of the salt with md5.

![alt text](solution/qns.png)


We will look at the main function:
![alt text](solution/salt.png)

and the check function:
![alt text](solution/hash.png)

We can see that there is a salt and a hash.
Then we proceed to using hashcat to crack the password: 
```.\hashcat64.exe -a 3 -m 20 .\hash_pass  --show```

#### In the event pastebin post gets taken down:
```
Name: YuanKai Lam
DOB: 01 April 2000
Class: DISM/34
Age: 18
Nickname: KaiKai
 
Crush: Apple Lim
DOB: 04 April 2000
Nickname: XiaoPingGuo
 
Pet: Jonathan Lam
```

Password: kaikai10004

### Flag
`GCTF{L3ts_G0_H4v3_fun}`
