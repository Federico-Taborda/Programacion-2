#include<stdio.h>
#include<string.h>

int main() {
    char cadena[100];
    char letra;
    int i = 0;

    printf("Ingrese un caracter\n");
    scanf(" %c", &letra);

    printf("Ingrese una cadena\n");
    scanf(" %[^\n]", cadena);

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
