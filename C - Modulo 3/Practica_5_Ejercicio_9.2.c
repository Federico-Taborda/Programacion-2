#include<stdio.h>

int main() {
    char *ptr = "hola mundo";
    ptr[0] = 's';
    printf("%s\n", ptr);
    return 0;
}

/*
La salida sera un error en tiempo de ejecucion Segmentation fault
Se asigna una cadena literal a un puntero
Las cadenas literales se guardan en una seccion de memoria solo de lectura
Cuando se intenta modificar el primer elemento de la cadena
ocurre un error al violar la restriccion de lectura
*/