#include<stdio.h>
#include<string.h>

int contarApariciones(char cadena[], char letra) {
    int contador = 0;

    for (int i = 0; i < strlen(cadena); i++) {
        if(cadena[i] == letra) contador++;
    }

    return contador;
}

int main() {
    char letra = 'a';
    char cadena[] = "palabra";
    int cantidad = contarApariciones(cadena, letra);

    printf("El caracter %c aparece %d veces en la cadena\n", letra, cantidad);

    return 0;
}


