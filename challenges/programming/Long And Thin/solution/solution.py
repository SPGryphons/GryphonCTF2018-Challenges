from PIL import Image
import numpy as np

im=Image.open("flag.png")
pic=im.load()
print(im.format, im.size, im.mode)

size=im.size
print(size)
width=size[0]
height=size[1]
print(width, height)

new_height=300
new_width=width/new_height

im2=Image.new("RGB",(new_width,new_height))
pic2=im2.load()
count = 0
for i in range(new_width):
	for j in range(new_height):
		pic2[i,j]=pic[count,0]
		count+=1
	
print(count)
im2.save("solve.png")
