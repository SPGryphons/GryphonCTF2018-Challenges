# Forest 2

## Question Text

The first one is a little easy eh? Well, this time, its a little dar-harder.

*Creator - Noans*

### Hints (Optional)
1. It's black. Just black

## Setup Guide
1. Run `virtualenv . && Scripts\activate && pip install -r requirements.txt` in [environment](generate/environment).
2. Go to [Pexel](https://www.pexel.com), make a search for some images.
3. While on the search page on Pexel, keep scrolling down to load more images.
4. Once you feel that there are enough images, download the page to the [generate](generate) directory.
5. Run `script.py`.
6. Edit appropriate images to place flag in them.
7. Run `update.py`.

For our purpose, we searched for `wild` on [Pexel](https://www.pexel.com)

## Distribution
- images-1.zip
    - SHA1: `77c0fcd20c65f71770472b4b437134da829a98c8`
- images-2.zip
    - SHA1: `7a261c33193b9a1176cb5c5054ca5a2520799567`
- images-3.zip
    - SHA1: `9232dc31e1825bf555ad8d52aaaf4947452799b0`
- images-4.zip
    - SHA1: `2f286853fcac3c39795f576c74daa99372e97a5f`

## Solution
In the zipped file, there are a total of 250 images. Within the 250 images, the flags are hidden in 4 of the images. Using the naked eye, it is unlikely that one will see the hidden flag, so we need a little help.

Since the hint says that the flag is black, taken literally, a [script](solution/filter.py) can be programmed to filter the pixels in the images and only show the parts which are black. Thereafter, opening the first image, `1.jpg`, we will see that the image contains part of the flag.

While we can choose to slowly scour through the rest of the images to find and piece together the other parts of the flag, we can also use a OCR library like Tesseract for Python to help us.
An example of the script which does the OCR can be seen [here](solution/ocr.py).

While the OCR wouldn't give perfect results due to compression done on the images, one can still use them to identify image which have text hidden in them.

Images containing flags are:
- 1.jpg
- 96.jpg
- 308.jpg
- 416.jpg
- 480.jpg
- 654.jpg
- 823.jpg

### Flag
`GCTF{0CR_15_4MAZING_T0_PL4Y_W1TH}`
