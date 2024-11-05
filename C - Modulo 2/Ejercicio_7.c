#include<stdio.h>
#include<string.h>

int main() {
    char cadena[6] = "bucle";
    int i = 5;
    char caracter = 't';

    for (; i > 0; i--) {
        // Guarda el caracter hasta el cual se debe mostrar
        char aux = cadena[strlen(cadena) - i + 1];

        // Cambia el caracter por el terminador de cadena
        cadena[strlen(cadena) - i + 1] = '\0';

        printf("%s %d %c\n", cadena, i, caracter);

        caracter -= 1;

        // Coloca nuevamente el caracter en su posicion
        cadena[strlen(cadena)] = aux;
    }
    
    return 0;
}