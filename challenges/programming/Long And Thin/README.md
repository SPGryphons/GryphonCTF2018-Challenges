# Long And Thin

## Question Text

Helppppppp! My image got squashed by a bulldozer. Please help me get back my beautiful image. P.S. my image was 300px high 

*Creator - WhiteLight*

## Setup Guide
Run `python generate.py` to generate the distrib image

## Solution

Given that the height of the original image is 300px, we can deduce that the width is also 300px. Using Python Imaging Library, we can reimage the given image into a 300x300 pixels image, which will give us an image of a QR code. By scanning the qr code, the flag will be shown

### Flag
`GCTF{5UCH_L0NG_1M4G3}`