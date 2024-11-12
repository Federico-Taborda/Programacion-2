#include<stdio.h>

int main() {
    int array[] = {1,2,3,4,5,6,7,8,9,10};
    int *ptr;
    ptr = array;
    printf("array[0]>%d; *ptr:%d\n", array[0], *ptr);
    printf("array[1]>%d; *(ptr + 1):%d\n", array[1], *(ptr+1));
    ptr++;
    printf("ptr++; *ptr: %d\n", *ptr);
    return 0;
}

/*
La funcion imprimira dos veces el primer elemento del array utilizando 
desplazamiento de memoria con el operador [] y desreferenciando el puntero ptr


La funcion imprimira dos veces el segundo elemento del array utilizando 
desplazamiento de memoria con el operador [] y usando aritmetica de punteros

Desplazara la memoria a la que apunta el punteo ptr una posicion hacia adelante
e imprimira su valor que es 2
*/