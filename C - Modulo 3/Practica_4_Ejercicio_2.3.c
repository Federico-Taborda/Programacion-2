#include<stdio.h>
#include<stdlib.h>

/*
Se declara una funcion copiar_cadena que recibe un puntero cad de tipo char
y un entero longitud y retorna un puntero de tipo char
Se declara un puntero a de tipo char
Se inicializa a pidiendo un bloque de memoria de tamaño char * longitud
Se itera por cada direccion de memoria del puntero a y se copia el valor de la
cadena cad en esa posicion
*/

char* copiar_cadena(char* cad, int longitud) {
    char* a = malloc(sizeof(char) * longitud);
    
    for(int i = 0; i < longitud; i++) {
        a[i] = cad[i];
    }

    return a;
}

int main() {
    char a[5] = "hola";
    char *b = copiar_cadena(a, 5);
    printf("%s %s\n", a, b);
    b[0] = 's';
    printf("%s %s\n", a, b);
    free(b);
    return 0;
}

/*
Se declara un array de de tipo char de tamaño 5 que contiene la cadena "hola"
Se declara un puntero b de tipo char y se inicializa con la salida de la funcion copiar_cadena
Se imprime por pantalla el contenido de a y b
Se reemplaza el valor de la primera posicion del puntero b por 's'
Se imprime por pantalla el contenido de a y b
Se libera el bloque de memoria pedido para el puntero b
*/
