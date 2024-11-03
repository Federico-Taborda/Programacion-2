#include<stdio.h>
#include<string.h>

// Invierte pero no compara correctamente
int main() {
    char cadena_ingresada[100];
    char cadena_invertida[100];
    int i, j;

    printf("Ingrese una cadena\n");
    scanf("%s", cadena_ingresada);

    i = strlen(cadena_ingresada) - 1;

    for(j = 0; i >= 0; i--, j++) {
        cadena_invertida[j] = cadena_ingresada[i];
    }

    cadena_invertida[j + 1] = '\0';

    printf("%s %s\n", cadena_ingresada, cadena_invertida);
    if (cadena_ingresada == cadena_invertida) {
        printf("%s es capicua\n", cadena_ingresada);
    }

    printf("%s no es capicua\n", cadena_ingresada);
    

    return 0;
}