#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void xor(char *input){
    unsigned char x[] = {105, 203, 60, 194, 95, 26, 212, 199, 241, 43, 211, 170, 88, 140, 10, 82, 191, 229, 19, 57, 200, 45, 211, 23};
    for (int i = 0; i < sizeof(x)/sizeof(x[0]); i++) {
        input[i] ^= x[i];
    }
}

int main(int argc, char* argv[]){
    unsigned char user_input[128];
    unsigned char flag[] = {46, 136, 104, 132, 36, 83, 139, 171, 152, 64, 150, 245, 111, 188, 85, 1, 136, 151, 122, 73, 151, 100, 228, 106};
    
    printf("====================\n");
    printf("Welcome to Strippy! \n");
    printf("====================\nFlag> ");

    fgets(user_input, sizeof(user_input), stdin);
    user_input[strcspn(user_input, "\r\n")] = 0;

    unsigned int input_length = strlen(user_input);

    if (input_length != 24) {
        printf("Not the flag :(\n");
        return 0;
    }

    xor(user_input);

    for (int i = 0; i < input_length; i++) {
        if (user_input[i] != flag[i]) {
            printf("Not the flag :(\n");
            return 0;
        }
    }

    printf("You got the flag!\n");
    return 0;
}