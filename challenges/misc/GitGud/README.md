# Git Gud

## Question Text

I could have sworn I stored something in my repository, but I can't seem to find my repository or what I stored anywhere?



### Hints (Optional)

I am a fan of taking notes, are you?

*Creator - whoami*

## Setup Guide

1. Extract the repository from the zip file
2. Push the repository to a Github account
3. Use command `git push origin "refs/notes/*"` to push the notes to the repository



## Solution

1. Clone the repository
2. Change directory to the repository and run `git fetch origin "refs/notes/*:refs/notes/*"` to fetch notes from the repository
3. Use `git log --show-notes="*"` or `git log --show-notes="*"` to get the flag