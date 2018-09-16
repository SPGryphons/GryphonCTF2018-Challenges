# TooTedious

## Question Text

We have managed to intercept the following images of stolen card numbers from a hacker.The flag seems to one of the card numbers..

However it seems like they are encrypted. 

Do your best to find the flag.

*Creator - kon8387*

### Hints (Optional)
1. Is there a computer programme to translate text on images to useable text

## Distribution
- CardNumbers.png
    - An Image of all 30 encrypted cards

## Solution
Optical Character Recognition aka OCR is a widely used technology that translate text in images into machine readable text.

Instead of typing each letter out manually,we can use OCR to convert the card numbers into machine readable text.

All the card numbers are encrypted with a simple caeser shift of 8 and can be decrypted the same way. 

### Flag
`GCTF{COMPU73R_3Y3}`

## Recommended Reads
* https://docparser.com/blog/what-is-ocr/
* https://learncryptography.com/classical-encryption/caesar-cipher