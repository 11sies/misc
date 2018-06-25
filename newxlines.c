#include <stdio.h>      // printf, fprintf
#include <stdlib.h>     // atoi

#define DEFAULT_LINE 24

void printline(char *line);

int main (int argc, char *argv[])
{

    if (argc < 2 || argc > 3){
        fprintf(stderr, "Error: wrong number of arguments\n");
        fprintf(stderr, "Usage: newxlines numlines [linelength]\n");
        exit(1);
    }


    int linelen = DEFAULT_LINE;         // length of lines
    if (argc == 3) linelen = atoi(argv[2]);
    char line[linelen];
    for (int i=0; i<linelen; i++)
        line[i] = '-';
    line[linelen] = '\0';

    int lines = atoi(argv[1]) - 2;      // number of lines to be printed
    int spaces = 1;
    printline(line);
    printline(line);
    while (lines > 0){
        for (int j=0; j<spaces; j++)
            printf("\n");
        printline(line);
        lines--;
        spaces *= 2;
    }
}

void printline(char *line){
    printf("%s\n", line);
}
