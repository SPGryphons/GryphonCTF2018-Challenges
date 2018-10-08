#include <stdio.h>
#include <string.h>

#define FLAG "GCTF{cann07_s7r1ng5_ch4r_4rr4y5}"

int validat0r() {
    char password[] = "7h15i5av3ry_v3ry_v3ry_v3ry_l0ng_p4ssw0rd_1otru0H1253";
    char input[64];

    char *fancyart = " _  _____ _/ (_)__/ /__ _/ /_/ _ \\____\n"
                     "| |/ / _ `/ / / _  / _ `/ __/ // / __/\n"
                     "|___/\\_,_/_/_/\\_,_/\\_,_/\\__/\\___/_/   \n"
                     "                                    v1\n"
                     "--------------------------------------\n";

    printf("%s", fancyart);
    printf("%s", "password pls > ");
    fgets(input, sizeof(input), stdin);
    input[strcspn(input, "\n")] = 0;

    if(strcmp(password, input) == 0) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    setbuf(stdout, NULL);
    if(validat0r()) {
        puts(FLAG);
    } else {
        puts("no");
    }
}