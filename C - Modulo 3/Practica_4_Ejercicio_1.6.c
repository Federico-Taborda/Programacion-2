#include<stdio.h>

/*
Se declara un array v de 4 enteros (2,4,5,7)
Se declara una variable a de tipo entero
Se declara un puntero p de tipo entero
Se guarda la direccion de memoria del tercer elemento del array v en el puntero p
Se retrocede una posicion en memoria a la que apunta p
Se le asigna a la variable a:
La suma del valor de p (4) mas p + 1 (5) mas v + 1 (4) mas p[2] (7)
Salida: 20
*/

int main() {
    int v[4] = {2,4,5,7}, a, *p;
    p = v + 2;
    p--;
    a = *p + *(p + 1) + *(v + 1) + p[2];
    printf("%d\n", a);
    return 0;
}