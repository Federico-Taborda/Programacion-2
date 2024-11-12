#include<stdio.h>


/*
Se declara una funcion direcciona_local que toma un entero y devuelve
la direccion de memoria del entero pasado como argumento
*/
int *direccion_local(int x) {
    return &x;
}

/*
Se declara un puntero ptr de tipo entero inizializado en Nulo
Se le asigna la salida de la funcion direccion local a ptr
Se imprime por pantalla el valor del puntero ptr
*/
int main() {
    int *ptr = NULL;
    ptr = direccion_local(2);
    printf("%d\n", *ptr);
    return 0;
}