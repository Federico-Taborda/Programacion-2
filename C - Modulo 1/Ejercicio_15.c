#include<stdio.h>

int maximo(int n, int m) {
    if(n > m) return n;
    return m;
}

int main() {
    int a, b, c, d, mayor;

    printf("Ingrese cuatro numeros: \n");
    scanf("%d%d%d%d", &a, &b, &c, &d);

    mayor = maximo(a, b);
    mayor = maximo(mayor, c);
    mayor = maximo(mayor, d);

    printf("El numero mayor es %d\n", mayor);

    return 0;
}