# My Name

## Question Text

Everybody
Has a name
Some are different 
Some the same 
Some are short 
Some are long
All are right
None are wrong 
I like my name 
It's special to me 
It's exactly who I want to be!
What's my name?


*Creator - Va1aR (Joshua)


## Setup Guide
1. Run `./build.sh` in the service directory.

## Solution
	
This challenge requires the user to figure out the person's name correctly
After entering the correct name, they will be able to retrive the flag

The user will see a wordsearch image when they are at index.jsp

They will also see:
"What is my name?"
"Enter my name to get the flag"

The wordsearch image contains the numbers: 0,14,14 
on the top left, top right, and bottom left corners respectively
These refer to "coordinates" of letters in the wordsearch image

With the help of the wordsearch image, the user must figure out the person's name.

After figuring out the name, the user must enter the name to retrieve the flag

The user can choose to look at hints if they feel that the task is too challenging

There are hints in index.jsp itself
Each hint displays an image as well as some text.

	
1. User must download and save the wordsearch png file
2. User must open the saved png file with Notepad
3. At the end, the user will see "USE THIS TO GET THE FLAG:	(49 , 58, 22 , 22 , 24 , 15 , 47)"
4. User must use the numbers as coordinates on the wordsearch png file.'49' means row 4 col 9
5. User will get the name "Cassidy"
6. User enters the name and gets the flag
	
Disclaimer:
	
	.toLowerCase() method is used at checkAnswer.jsp to change user input to lower case
	


### Flag
`GCTF{F1V3_N1GHT5_4T_FR3ddY'5}`

