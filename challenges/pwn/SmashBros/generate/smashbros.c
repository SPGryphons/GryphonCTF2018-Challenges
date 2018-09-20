#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void vuln(){
    char buf[32];
    printf("> ");
    gets(buf);
    printf("Bye\n");
}
int main(int argc, char* argv[]){
    // Disable output buffering
    setbuf(stdout, NULL);

    printf("=====================\n");
    printf("Welcome to Smash Bros\n");
    printf("=====================\n");
    printf("Here is your leaked LIBC address\nstdin: %p\n", stdin);
    vuln();
    return 0;
}