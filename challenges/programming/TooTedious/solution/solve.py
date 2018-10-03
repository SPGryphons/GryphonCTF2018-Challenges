from PIL import Image
# install pytesseract if you haven't alr
import pytesseract

L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

im = Image.open("CardNumbers.png")

text = pytesseract.image_to_string(im)

decryptedtext = ""

key = 8

#loop to shift all letters by -8, thus decoding the text
for c in text.upper():
	if c.isalpha(): decryptedtext += I2L[ (L2I[c] - key)%26 ]
	else: decryptedtext += c

start = decryptedtext.find('GCTF{')
end = decryptedtext.find('}', start)+1
print ("The flag is --> "+ decryptedtext[start:end])


#print (decryptedtext)
#print(text)
