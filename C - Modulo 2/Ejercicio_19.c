#include<stdio.h>
#include<string.h>

int contar_caracter(char cadena[], char caracter) {
    int contador = 0;
    
    for (int i = 0; i < strlen(cadena); i++) {
        if(cadena[i] == caracter) contador++;
    }

    return contador;
}

int main() {
    char cadena[] = "";
    char caracter;
    int contador = 0;

    printf("Ingrese una cadena y un caracter\n");
    scanf("%s %c", cadena, &caracter);

    contador = contar_caracteres(cadena, caracter);

    printf("El caracter %c aparece %d veces en %s\n", caracter, contador, cadena);

    return 0;
}


