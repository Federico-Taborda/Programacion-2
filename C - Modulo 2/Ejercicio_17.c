#include <stdio.h>

#define N = 1000;

int main() {
    // Declara dos enteros y un arrglo de enteros de tamaño N + 1 (1000 + 1)
    int i, j, a[1000 + 1];

    // Itera el arreglo a desde la posicion 1 hasta N
    for (a[1]=0 , i=2; i <= 1000; i++) {
        // Guarda un numero entero (1) en la posicion i del arreglo a
        a[i] = 1;
    }

    //  Itera el arreglo a desde la posicion 2 hasta N/2
    for (i=2; i <= 1000/2; i++) {
        // Itera el arreglo a desde la posicion 2 hasta 1000/i
        for (j=2; j <= 1000/i; j++) {
            // Guarda un numero entero (0) en la posicion i*j
            a[i*j] = 0;
        }
    }

    // Itera el arreglo a desde la posicion 1 hasta N
    for (i=1; i <= 1000; i++) {
        // Si la posicion i del arreglo a es 1 imprimira su valor
        if(a[i]== 1) {
            printf("%d", i);
        }
    }

    // Imprime un salto de linea alfinal del programa
    printf("\n");
    return 0;
}