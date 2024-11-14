#include<stdio.h>
#include<string.h>

int contar_caracter(char cadena[], char caracter) {
    int contador = 0;
    
    for (int i = 0; i < strlen(cadena); i++) 
        if(cadena[i] == caracter) 
            contador++;

    return contador;
}

int contar_recursivo(char cadena[], char caracter, int indice, int contador) {
    if(cadena[indice] == '\0') return contador;

    if(cadena[indice] == caracter)
        contador++;

    return contar_recursivo(cadena, caracter, indice + 1, contador);
}

int main() {
    char cadena[] = "";
    char caracter;
    int contador = 0;

    printf("Ingrese una cadena\n");
    scanf(" %[^\n]", cadena);

    printf("Ingrese un caracter\n");
    scanf(" %c", &caracter);

    //contador = contar_caracter(cadena, caracter);
    contador = contar_recursivo(cadena, caracter, 0, 0);
    printf("El caracter %c aparece %d veces en %s\n", caracter, contador, cadena);

    return 0;
}


