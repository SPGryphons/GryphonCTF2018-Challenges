# Git Gud

## Question Text

I could have sworn I stored something in my repository, but I can't seem to find my repository or what I stored anywhere?



### Hints (Optional)

I am a fan of taking notes, are you?

*Creator - whoami*


## Solution
1. Search for the repository first on Github using the challenge name 'Git Gud'
2. Clone the repository
3. Change directory to the repository and run `git fetch origin "refs/notes/*:refs/notes/*"` to fetch notes from the repository
4. Use `git log --show-notes="*"` or `git log --show-notes="*"` to get the flag
