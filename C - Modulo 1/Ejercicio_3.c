#include<stdio.h>

int main() {
    float x, y;
    printf("Introduzca 2 numeros:\n");
    scanf("%f%f", &x, &y);
    printf("La suma de %f y %f vale %f\n", x, y, x +y);
    printf("La suma de %4f y %4.2f vale %10.3f\n", x, y, x +y);
    printf("La suma de %e y %e vale %e\n", x, y, x +y);
    return 0;
}

// Si se ingresaran 1 y 2 la salida seria:
// La suma de 1.000000 y 2.000000 vale 3.000000
// La suma de 1.000000 y 2.00 vale      3.000
// La suma de 1.000000e+00 y 2.000000e+00 vale 3.000000e+00