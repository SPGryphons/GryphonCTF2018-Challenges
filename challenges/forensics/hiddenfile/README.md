# hiddenfile

## Question Text

There seems to be some hidden files within the .rar. Hmmmm Where could they be?.

### Disclaimer
Use Microsoft OS(Windows 7 or higher), 
Filesystem of OS must be NTFS, 
Use winrar to extract the contents.

*Creator - kon8387*

### Hints (Optional)
1. How can NTFS hide files?
2. Did you look at EVERYTHING in the rar file?

## Distribution
- hiddenfile.rar
    - SHA1: `2FBE4A7D0EE7054A02ADBC9770F3A75181C2DCE1`


## Solution
Alternate Data stream in the NTFS file system allows you to store data in a seperate stream "behind" any filename. Hence the name Alternate Data Stream or ADS. This makes it hard to detect hidden files using normal methods.

1. Open a command prompt.
2. To detect the files first type in "dir /r *fullpath to extracted folder*".
3. You should be see a bunch of hidden files including the `:flag.txt` file.
4. The `:flag.txt` is located behind the folder named file.
5. To view the contents of the `:flag.txt` file we can use the command "notepad folder:flag.txt" (Include the full pathname to the folder if your not in the same directory).
6. A notepad containing the flag should show up.



### Flag
`GCTF{N7F5_H1DD3N_F1L35}`

## Recommended Reads
* https://blog.malwarebytes.com/101/2015/07/introduction-to-alternate-data-streams/
* https://www.howtogeek.com/howto/windows-vista/stupid-geek-tricks-hide-data-in-a-secret-text-file-compartment/
