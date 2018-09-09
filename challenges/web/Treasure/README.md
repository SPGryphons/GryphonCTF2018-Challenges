# Treasure

## Question Text

I found this treasure chest but I can't open it!!!

*Creator - PotatoDrug*

### Hints (Optional)
1. There is a tool to unpack the code

## Setup Guide
Run `./build.sh`

## Solution

The first line of code in script.js is basically getting user input and calling the check function to check if the key entered is correct. The next line of code is packed using a [packer](http://dean.edwards.name/packer/) which can be unpacked using [this](http://matthewfl.com/unPacker.html). The unpacked output is shown below.
```javascript
function check(b) {
    if(!b.match(/GCTF{.*}/))return false;
 
    let a=/¤À.áÔ¥6¦Ó¹WþÊmãÖÚG¤7ùª9¨Mªћ#³­1᧨ẋ2¨Ӈ#ṡ2Ṣ€Ç³Ç¤œ&¬ɓÓÂ.Ö£¢dÈ9&Jºò³=SȯẊÇ¿/;

    for(let i=0;i<a.length;i++) {
        b[i]=String.fromCharCode(b[i%b.length]^a[i%b.length].charCodeAt(0)>>1<<2%68+1)
    }

    return b.split('').map(c=>(c.charCodeAt(0)<<1^0x12)>>1^0xa1).toString()===[239,235,252,238,211,194,156,254,156,157,203,250,153,216,220,247,153,157,247,217,221,153,220,155,247,235,156,198,203,155,250,199,253,157,213].toString();
}
```
The first if condition checks if the input is in valid flag format.

This part actually does nothing as the for loop will not run because a has no length since it is a regex and not a string.
```javascript
    let a=/¤À.áÔ¥6¦Ó¹WþÊmãÖÚG¤7ùª9¨Mªћ#³­1᧨ẋ2¨Ӈ#ṡ2Ṣ€Ç³Ç¤œ&¬ɓÓÂ.Ö£¢dÈ9&Jºò³=SȯẊÇ¿/;

    for(let i=0;i<a.length;i++) {
        b[i]=String.fromCharCode(b[i%b.length]^a[i%b.length].charCodeAt(0)>>1<<2%68+1)
    }
```

The last part of the function does some bitwise operations on each byte of the input key.

1. left shift by 1
2. xor with `0x12`
3. right shift by 1
4. xor with `0xA1`

Then it compares the result with the stored values, if they are the same then the flag is valid.

So we simply need to reverse the bitwise operations on the stored values to get the flag.

[CyberChef](https://gchq.github.io/CyberChef/) recipe
```
Fork(',','',false)
From_Decimal('Space')
XOR({'option':'Hex','string':'A1'},'Standard',false)
Bit_shift_left(1)
XOR({'option':'Hex','string':'12'},'Standard',false)
Bit_shift_right(1,'Logical shift')
```

### Flag
`GCTF{j4V45cR1pt_15_qu1t3_C4nc3RoU5}`
