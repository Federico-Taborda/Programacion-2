#include<stdio.h>

int main() {
    int n;
    int pasos = 0;

    printf("Ingrese un numero positivo\n");
    scanf("%d", &n);

    for (; n > 1; pasos++) {
        if(n % 2 == 0) {
            n /= 2;
        }else{
            n = (n * 3) + 1;
        }
        printf("El siguiente valor es %d\n", n);
    }

    printf("Valor final %d, numero de pasos %d\n", n, pasos);

    return 0;
}