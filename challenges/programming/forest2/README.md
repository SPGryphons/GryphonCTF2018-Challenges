# Forest 2

## Question Text

The first one is a little easy eh? Well, it isn't so easy this time. The flag is black :)

*Creator - Noans*

### Hints (Optional)
1. OCR

## Distribution
- images.zip
    - SHA1: `c401299d6d1a5cf6f26fc688bdd4838cffeaa4f3`

## Solution
In the zipped file, there are a total of 250 images. Within the 250 images, the flags are hidden in 4 of the images. Using the naked eye, it is unlikely that one will see the hidden flag, so we need a little help.

Since the question says that the flag is black, taken literally, a [script](solution/filter.py) can be programmed to filter the pixels in the images and only show the parts which are black. Thereafter, opening the first image, `1.jpg`, we will see that the image contains part of the flag. While we can choose to slowly scour through the rest of the images to find and piece together the other parts of the flag, we can also use a OCR library like Tesseract for Python to help us.

An example of the script which does the OCR can be seen [here](solution/ocr.py).

Images containing flags are
- 1.jpg
- 36.jpg
- 93.jpg
- 180.jpg


### Flag
`GCTF{0CR154MAZING}`

## Recommended Reads
* https://links.to.good.reads
* https://www.example.com
