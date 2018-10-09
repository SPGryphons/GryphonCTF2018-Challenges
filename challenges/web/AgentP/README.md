# Agent P

## Question Text

"He is a platypus, they don't do much."

*Creator - @exetr (Chuan Kai)*

### Hints
1. Screw firefox and chrome, my favourite browser is IE4 :P

## Setup Guide

Run `./build.sh`

## Solution

Doing a `curl web.chal.gryphonctf.com:18706`, we can see the following

```
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>perry the platypus 4</title>
</head>

<body>
    <img src="perry_the_platypus.png" alt="perry the platypus">
</body>

</html>
<br>curl/7.58.0<br>This is not my favourite browser :(, i prefer something more... antiquated and preferably by Microsoft
```

At the very bottom, the user agent string is printed, which is the direction towards solving this challenge. However, knowing which version of IE may require a bit of elbow grease.

The version of IE which will result in the flag being printed is any version of Internet Explorer 4. While it cannot be downloaded and run (easily) anymore, you can modify the user agent string wtih curl. Do note that any version before 4 would also work.

```
~$ curl -A "Mozilla/4.0 (Compatible; MSIE 4.0)" http://web.chal.gryphonctf.com:18706
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>perry the platypus 4</title>
</head>

<body>
    <img src="perry_the_platypus.png" alt="perry the platypus">
</body>

</html>
<br>Mozilla/4.0 (Compatible; MSIE 4.0)<br>GCTF{gr347_j0b_AgEnT_p!}
```

### Flag
`GCTF{gr347_j0b_AgEnT_p!}`


## Recommended Reads
- http://www.useragentstring.com/pages/useragentstring.php?name=Internet+Explorer
