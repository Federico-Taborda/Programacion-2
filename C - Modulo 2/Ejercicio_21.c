#include<stdio.h>
#include<string.h>

int main() {
    char cadena_ingresada[100];
    int i, j, len = 0;

    printf("Ingrese una cadena\n");
    scanf("%s", cadena_ingresada);

    i = strlen(cadena_ingresada) - 1;

    for(j = 0; i >= 0; i--, j++) {
        if(cadena_ingresada[j] == cadena_ingresada[i]) len++;
    }

    if (len == strlen(cadena_ingresada)) {
        printf("%s es capicua\n", cadena_ingresada);
        return 0;
    }

    printf("%s no es capicua\n", cadena_ingresada);
    return 0;
}