#include<stdio.h>
#include<string.h>

int main() {
    char cadena_ingresada[100];
    char cadena_invertida[100];
    int i, j;

    printf("Ingrese una cadena\n");
    scanf("%[^\n]", cadena_ingresada);

    i = strlen(cadena_ingresada) - 1;

    for(j = 0; i >= 0; i--, j++) {
        cadena_invertida[j] = cadena_ingresada[i];
    }

    cadena_invertida[j + 1] = '\0';

    printf("Cadena original: %s\n", cadena_ingresada);
    printf("Cadena invertida: %s\n", cadena_invertida);

    return 0;
}
