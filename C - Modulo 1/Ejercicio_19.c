#include<stdio.h>

int fibonacci(int n) {
    if(n == 0) return 0;

    if(n == 1) return 1;

    if(n > 2) return fibonacci(n - 1) + fibonacci(n - 2);

    return 0;
}


int main() {
    int n, resultado;

    printf("Ingrese un numero: \n");
    scanf("%d", &n);

    resultado = fibonacci(n);

    printf("El resultado es %d\n", resultado);

    return 0;
}