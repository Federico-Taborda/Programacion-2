#include<stdio.h>
#include<string.h>

int main() {
    char cadena[100];
    char reves[100];
    int i, j;

    printf("Ingrese una cadena\n");
    scanf("%s", cadena);

    i = strlen(cadena) - 1;

    for(j = 0; i >= 0; i--, j++) {
        reves[j] = cadena[i];
    }

    reves[j + 1] = '\0';

    printf("Cadena original: %s\n", cadena);
    printf("Cadena invertida: %s\n", reves);

    return 0;
}
