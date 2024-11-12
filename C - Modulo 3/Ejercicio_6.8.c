#include<stdio.h>
#include<stdlib.h>

// No se que es fgets ni stdin
void ingreseCadena(char* c) {
    fgets(c, 10, stdin);
}

int main() {
    char* cadena = malloc(sizeof(char) * 10);
    fgets(cadena, 10, stdin);
    printf("%s\n", cadena);
    ingreseCadena(cadena);
    printf("%s", cadena);
    free(cadena);
    return 0;
}