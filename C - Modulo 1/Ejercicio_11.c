#include<stdio.h>

int main() {
    int n, m;
    printf("Ingrese dos numeros: \n");
    scanf("%d%d", &n, &m);

    while(n > m) {
        printf("El primero debe ser mayor que el segundo: \n");
        scanf("%d%d", &n, &m);
    }

    while(n <= m) {
        printf("%d\n", n);
        n++;
    }

    return 0;
}