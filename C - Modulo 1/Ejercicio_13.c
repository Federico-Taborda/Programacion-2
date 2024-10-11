#include<stdio.h>

int factorial(int n) {
    if(n == 0) {
        return 1;
    }

    return n * factorial(n - 1);
}

int main() {
    int a = 0;
    int b = 0;

    printf("Ingrese un numero\n");
    scanf("%d", &a);

    b = factorial(a);

    printf("El factorial de %d es %d", a, b);
    return 0;
}