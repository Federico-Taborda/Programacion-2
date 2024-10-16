#include<stdio.h>

int maximo(int n, int m) {
    if(n > m) return n;
    return m;
}

int main() {
    int a, b, c, mayor;

    printf("Ingrese tres numeros: \n");
    scanf("%d%d%d", &a, &b, &c);

    mayor = maximo(a, b);
    mayor = maximo(mayor, c);

    if(a + b + c - mayor > mayor)  return 1;

    return 0;
}