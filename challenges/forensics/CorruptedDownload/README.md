# Corrupted Download

## Question
I wanted to see how a cinnamon roll looks like, so what better way than to download it! But something went wrong when I was downloading it and I can't view the image.
I think it may be corrupted or something. Help me see my cinnamon roll and I'll reward you for it!

*Creator - whoami* 

## Hint
Something about the start and end of the image looks off don't you think?

## Distribution
* [cinnamonroll.jpg](Distrib/cinnamonroll.jpg)
  * SHA-1: 87ADD9E463B591B0FD91D374F915EBEBC097638A

## Solution
The file is a JFIF image and the Start of Image, End of Image markers have been replaced by 00. Use a hex editor and add FF D8 and FF D9 for the SOI and EOI markers and the flag can be found in the bottom right of the image

## Flag
GCTF{Jp3G_1S_t00_Ea5y_4_u}
