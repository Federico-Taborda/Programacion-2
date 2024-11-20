#include<stdio.h>
#include<stdlib.h>

/* 
Lee un cadena por entrada hasta 10bytes
 */
void ingreseCadena(char* c) {
    fgets(c, 10, stdin);
}

/* 
Se declara un puntero cadena de tipo char y se le asina dinamicamente 10btyes de tamaño
Lee un cadena por entrada hasta 10bytes
Imprime la cadena por consola
Se ejecuta la funcion ingresarCadena pasandole como argumento el puntero cadena
Se muestra por consola el valor de cadena
Se libera el bloque de memoria de puntero candena
 */

int main() {
    char* cadena = malloc(sizeof(char) * 10);
    fgets(cadena, 10, stdin);
    printf("%s\n", cadena);
    ingreseCadena(cadena);
    printf("%s", cadena);
    free(cadena);
    return 0;
}