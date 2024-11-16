#include<stdio.h>
#include<stdlib.h>

void setzerozero(int arr[]) {
    arr[0] = 4;
}

int main() {
    int array[3] = {1,2,3};

    printf("array:%d\n", array[0]);

    setzerozero(array);

    printf("array:%d\n", array[0]);

    return 0;
}

/*
Esto es posible porque un array es un puntero asi mismo, al pasar array como
argumento a la funcion setzerozero lo que se esta pasando es la direccion de 
memoria en donde se encuentra mismo array la cual coincide con la direccion
de memoria del primer elemento del array
*/