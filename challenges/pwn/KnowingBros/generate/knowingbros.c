#include <stdio.h>
#include <string.h>
#include <stdlib.h>
void sendknowledge(){
    char buf[32];
    printf("Knowledge > ");
    scanf("%s", buf);
    printf("Nice Knowledge\n");
}
void echo() {
    char buf[12];
    printf("Echo > ");
    fgets(buf,sizeof buf,stdin);
    printf(buf);
}
int main(int argc, char* argv[]){
    // Disable output buffering
    setbuf(stdout, NULL);

    printf("=======================\n");
    printf("Welcome to Knowing Bros\n");
    printf("=======================\n");

    char cmd[3];
    while (1) {
        printf("\n0: Echo\n1: SendKnowledge\n2: Exit\n> ");
        fgets(cmd,sizeof cmd,stdin);
        if (strcmp(cmd, "0\n") == 0) {
            echo();
        } else if (strcmp(cmd, "1\n") == 0) {
            sendknowledge();
        } else if (strcmp(cmd, "2\n") == 0) {
            printf("Bye Bye\n");
            exit(0);
        } else {
            printf("Invalid option\n");
        }
    }

    return 0;
}