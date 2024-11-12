#include<stdio.h>

/*
Se declara un puntero punt de tipo entero
Se declara una variable i de tipo entero
Se declara un array de enteros de 1 a 5
Se guarda la direccion de memoria del cuarto elemento del array x en el puntero punt
Se le asigna el valor 9 al segundo elemento del array x mediante aritmetica de punteros
Se retrocede una posicion de memoria del puntero punt
Se le asigna el valor 7 al tercer elemento del array x mediante aritmetica de punteros
Se le asigna el valor 11 al cuarto elemento del array x
Se le asigna la direccion de memoria del primer elemento del array x al puntero punt
Se itera sobre todos los elementos del array y se los imprime por pantalla
*/

int main() {
    int* punt, i;
    int x[] = {1,2,3,4,5};
    punt = &x[0] + 3;
    *(punt - 2) = 9;
    punt--;
    *(punt) = 7;
    punt[1] = 11;
    punt = x;
    for (i = 0; i < 5; i++) {
        printf("%d\n", punt[i]);
    }
    return 0;
}