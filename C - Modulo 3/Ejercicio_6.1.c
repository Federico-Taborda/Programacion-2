#include<stdio.h>

/* 
Se declara un puntero punt de tipo entero
Se declara un entero x inicializado en 7 y un entero y inicializado en 5
Se asigna la direccion de memoria de la variable x al puntero punt
Se le asigna 4 al valor al que apunta el puntero punt el cual es la direccion
de memoria de la variable x
Se imprime el valor de x e y los cuales son 4 y 5
*/

int main() {
    int *punt;
    int x = 7, y = 5;
    punt = &x;
    *punt = 4;
    printf("%d %d\n", x, y);
    return 0;
}