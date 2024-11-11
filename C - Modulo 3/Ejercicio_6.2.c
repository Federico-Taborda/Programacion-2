#include<stdio.h>

/* 
Se declara un puntero punt de tipo entero
Se declara un entero x inicializado en 7 y un entero y inicializado en 5
Se rescribe el valor de x a 4
Se asigna la direccion de memoria de la variable y al puntero punt
Se imprime el valor de punt y x los cuales son 5 y 4
*/

int main() {
    int *punt;
    int x = 7, y = 5;
    x = 4;
    punt = &y;
    printf("%d %d\n", *punt, x);
    return 0;
}