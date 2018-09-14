The name of this challenge is "MyName"

The user will see a wordsearch image when they are at index.jsp

The wordsearch image contains the numbers: 0,14,14 
on the top left, top right, and bottom left corners respectively
These refer to "coordinates" of letters in the wordsearch image

With the help of the wordsearch image, the user must figure out the person's name.

After figuring out the name, the user must enter the name to retrieve the flag

The user can choose to look at hints if they feel that the task is too challenging

There are hints in index.jsp itself
Each hint displays an image as well as some text.

Solution:
	
	1.	User must download and save the wordsearch png file
	2.	User must open the saved png file with Notepad
	3.	At the end, the user will see "USE THIS TO GET THE FLAG:	(49 , 58, 22 , 22 , 24 , 15 , 47)"
	4.	User must use the numbers as coordinates on the wordsearch png file.'49' means row 4 col 9
	5.	User will get the name "Cassidy"
	6.	User enters the name and gets the flag "GCTF{F1V3_N1GHT5_4T_FR3ddY'5}"
	
Disclaimer:
	
	.toLowerCase() method is used at checkAnswer.jsp to change user input to lower case
	


