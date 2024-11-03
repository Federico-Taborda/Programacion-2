#include<stdio.h>
#include<math.h>

int maximo(int n, int m) {
    if(n > m) return n;
    return m;
}

int esRectangulo(int a, int b, int c) {
    int mayor;

    mayor = maximo(a, b);
    mayor = maximo(mayor, c);

    if(pow(mayor, 2) == pow(a, 2) + pow(b, 2) + pow(c, 2) - pow(mayor, 2))  return 1;

    return 0;
}

int main() {
    int a, b, c, resultado;

    printf("Ingrese tres numeros: \n");
    scanf("%d%d%d", &a, &b, &c);

    resultado = esRectangulo(a, b, c);

    printf("Es rectangulo? %d\n", resultado);

    return 0;
}