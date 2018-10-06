#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

// prototypes
void printStuff(char*);
void doStuff();
char* randomOutput();
char* getInput();

int main(int argc, char** argv) {
    srand(time(NULL));
    setvbuf(stdin, NULL, _IONBF, 0);
    setbuf(stdout, NULL);

    doStuff();

    return 0;
}

void doStuff() {
    printf("What's your name: ");
    char buffer[30];
    scanf("%s", buffer);

    char* ptr = randomOutput();
    printf(ptr, buffer);
}

void interestingFunction() {
    printf("GCTF{0V3R_7H3_L1M17}");
    return;
}

char* randomOutput() {
    const char* greetings[5];

    greetings[0] = "Howdy! %s\n";
    greetings[1] = "All good? %s\n";
    greetings[2] = "Hello there %s!\n";
    greetings[3] = "Have a great day, %s!\n";
    greetings[4] = "Good day %s!\n";

    return greetings[rand() % 5];
}
