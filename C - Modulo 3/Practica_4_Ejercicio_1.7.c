#include<stdio.h>

/*
Se reciben tres parametros dos punteros x e y ademas de un entero z
Se le asigna el valor de la suma de x + 2 a el puntero x
Se le asigna el valor de la suma de y + 5 a el puntero y
Se le asigna el valor de la suma de z + 4 a z
*/
void aumentar(int* x, int* y, int z) {
    *x = *x + 2;
    *y = *y + 5;
    z = z + 4;
}

/*
Se declara tres variables x y z de tipo entero
Se le asigna el valor de 3 a x
Se le asigna el valor de 10 a y
Se le asigna el valor de z a 15
Se le pasa como argumento la direccion de memoria de x e y junto el valor de z
a la funcion aumentar
Se imprimen el valor de x y z por pantalla
5 15 15
*/

int main() {
    int x, y, z;
    x = 3;
    y = 10;
    z = 15;
    aumentar(&x, &y, z);
    printf("%d %d %d\n", x, y, z);
    return 0;
}