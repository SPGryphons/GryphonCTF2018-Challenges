#include <stdlib.h>
#include <string.h>
#include <stdio.h>

struct user {
  char name[32];
  int isadmin;
};

struct user *userptr;
char *prompt = ">";

int main(int argc, char *argv[]) {
  // Disable output buffering
  setbuf(stdout, NULL);
  char line[128];

  printf("___________        .__    __                              __   .__     \n");
  printf("\\_   _____/_____   |  |  |  | _________   ____  _____   _/  |_ |  |__  \n");
  printf(" |    __)  \\__  \\  |  |  |  |/ /\\_  __ \\_/ __ \\ \\__  \\  \\   __\\|  |  \\ \n");
  printf(" |     \\    / __ \\_|  |__|    <  |  | \\/\\  ___/  / __ \\_ |  |  |   Y  \\\n");
  printf(" \\___  /   (____  /|____/|__|_ \\ |__|    \\___  >(____  / |__|  |___|  /\n");
  printf("     \\/         \\/            \\/             \\/      \\/             \\/\n");

  while(1) {
    if (userptr == NULL) {
      printf("Not logged in\n%s", prompt);
    } else {
      printf("User: %s\n%s", userptr->name, prompt);
    }

    if(fgets(line, sizeof(line), stdin) == NULL) {
      break;
    }

    if(strncmp(line, "login ", 6) == 0) {
      userptr = calloc(1, sizeof(struct user));
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
    } else if (strcmp(line, "help\n") == 0) {
      printf("Commands available\n------------------------\nlogin <user>\nlogout\nprompt <new prompt>\ngetflag\nexit\n------------------------\n");
    } else if (strcmp(line, "exit\n") == 0) {
      break;
    } else {
      printf("Invalid command type `help` to see list of commands available.\n");
    }
  }

  return 0;
}