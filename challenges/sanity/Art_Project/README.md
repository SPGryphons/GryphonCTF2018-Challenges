# Art Project

## Question Text

The school holidays are almost over but I still haven’t completed my art project.

Rushing homework at the end of the holidays seems like tradition to me …

The flag is somewhere amongst the uncompleted pictures, try your best to find it.

*Creator - kon8387*

### Hints (Optional)
1. The cake is not a lie

## Distribution
- Art_Project.zip
    - SHA1: `4926705825A4B573D92B964CDABAFD4C61FAC6EE`

## Setup Guide
1. Piet images generated from `http://wallach.netsoc.ie/Piet/textToPiet.html`.


## Solution
The colour borders around each image is actually a programming language called piet, piet is a programming language that uses colour pixels to write programs and scripts. Piet is an esoteric programming language so the order of changes in hue and darkness of a colour corresponds to a command executed by the programme. (Eg. push command = darker by 1)

To solve the challenge you can upload the `cake.png` image to `https://www.bertnase.de/npiet/npiet-execute.php` to run the piet program and retrieve the flag `GCTF{P13T_Art_1S_N33T}`. 

or

You can download the npiet interpreter from `https://www.bertnase.de/npiet/` and run the command 'npiet.exe cake.png' in a terminal to execute the piet program. The flag `GCTF{P13T_Art_1S_N33T}` will show up in the terminal, Ctrl + C to stop the program.

A copy of the tool npiet for windows can be found in the solution folder.

### Flag
`GCTF{P13T_Art_1S_N33T}`

## Recommended Reads
* http://www.dangermouse.net/esoteric/piet.html
* https://youtu.be/4kH4T8uwHMw
* http://homepages.vub.ac.be/~diddesen/piet/index.html
