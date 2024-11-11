#include<stdio.h>

/* 
Se declara un puntero punt de tipo entero
Se declara un entero i;
Se declara un array x de cinco elementos 1,2,3,4,5
Se le asigna la direccion de memoria de x al puntero punt
Se le asigna el valor de 9 al primer elemento del array x
Se declara un bucle for que iterar en todos los elementos del array 
y los imprime uno por uno de la siguiente manera
- 9
- 2
- 3
- 4
- 5

*/

int main() {
    int *punt, i;
    int x[] = {1,2,3,4,5};
    punt = x;
    *punt = 9;
    for (i = 0; i < 5; i++) {
        printf("%d, \n", x[i]);
    }
    return 0;
}