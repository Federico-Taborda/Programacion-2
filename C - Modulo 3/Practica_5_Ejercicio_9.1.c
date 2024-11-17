#include<stdio.h>

void nullify(int* a) {
    a = NULL;
}

int main() {
    int a[67];
    a[0] = 123;
    printf("%d\n", a[0]);
    nullify(a);
    printf("%d\n", a[0]);
    return 0;
}

/*
El codigo imprimira 123 y 123
Se imprime el valor del primer elemento de a que es 123
Se pasa a como argumento a nullify
Dentro de nullify se asigna NULL a al array a pero solo afecta localmente
Luego se imprime el primer elemento de a que sigue siendo 123
*/