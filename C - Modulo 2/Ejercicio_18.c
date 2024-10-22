#include<stdio.h>
#include<string.h>

int main() {
    char letra = 's';
    char cadena[] = "palabra";
    int i = 0;

    while(cadena[i] != letra && i < strlen(cadena)) {
        i++;
    }

    if(i < strlen(cadena)) {
        printf("El caracter %c esta en la cadena\n", letra);
        return 0;
    }

    printf("El caracter %c no esta en la cadena\n", letra);
    return 1;
}
