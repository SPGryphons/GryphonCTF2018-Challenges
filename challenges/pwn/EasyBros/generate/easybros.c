#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void vuln(){
    char buf[128];
    printf("> ");
    gets(buf);
    printf("Bye\n");
}
int main(int argc, char* argv[]){
    // Disable output buffering
    setbuf(stdout, NULL);
    printf("====================\n");
    printf("Welcome to Easy Bros\n");
    printf("====================\n");
    vuln();
    return 0;
} 