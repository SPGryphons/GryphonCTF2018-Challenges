from PIL import Image
import numpy as np

im=Image.open("qr.png")
pic=im.load()
print(im.format, im.size, im.mode)

size=im.size
print(size)
width=size[0]
height=size[1]
print(width, height)

new_height=1
new_width=height*width

im2=Image.new("RGB",(new_width,new_height))
pic2=im2.load()
count = 0
for i in range(width):
	for j in range(height):
		pic2[count,0]=pic[i,j]
		count+=1
	
print(count)
im2.save("flag.png")
