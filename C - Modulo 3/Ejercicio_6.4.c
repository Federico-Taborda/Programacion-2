#include<stdio.h>

/*
Se declara un puntero punt de tipo entero
Se declara una variable i de tipo entero
Se declara un array x de enteros desde 1 a 5
Se guarda la direccion de memoria del arreglo x en el puntero punt
Se le asigna el valor 9 al tercer elemento del array x mediante aritmetica de punteros
Se le asigna el valor 7 al cuarto elemento del array x mediante aritmetica de punteros
Se le asigna el valor 11 al segundo elemento del array x
Se itera sobre todos los elementos del array e imprime su valor mediante aritmetica de punteros
*/

int main() {
    int* punt, i;
    int x[] = {1,2,3,4,5};
    punt = x;
    *(punt + 2) = 9;
    *(x + 3) = 7;
    punt[1] = 11;
    for (i = 0; i < 5; i++) {
        printf("%d\n", *(punt + i));
    }
    return 0;
}