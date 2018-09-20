from PIL import Image
# Requires Pillow to function

def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])

image = Image.open("trash.png")
binnumbers = ''
pixs = image.load()
for y in range(1600):
    for x in range(1200):
        if pixs[x,y] == (0,0,128):
            binnumbers += '0'
        elif pixs[x,y] == (128,0,0):
            binnumbers += '1'

print(toString(binnumbers))
