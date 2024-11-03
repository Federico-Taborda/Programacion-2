#include <stdio.h>

#define MAX_LONGITUD 100

/*


[  1   2   3 997 998 999]
-> revertir todo
[999 998 997   3   2   1]










[   1   2   3 997 998 999 ]
-> revertir primera parte
[   3   2   1 997 998 999 ]
-> revertir segunda parte
[   3   2   1 999 998 997 ]
-> revertir todo
[ 997 998 999   1   2   3 ]









    
arreglo ---> [   1   2   3 997 998 999 ]
                            ^
                            |
arreglo + k ----------------|






*/


void revertir(int *arreglo, int longitud);

void rotar(int *arreglo, int longitud, int k);

int main() {
    

    printf("Ingrese la longitud del arreglo (<= %d)\n", MAX_LONGITUD);
    int longitud;
    scanf("%d", &longitud);
    if (longitud < 0 || longitud > MAX_LONGITUD) {
        printf("Longitud invalida.\n");
        return 1;
    }

    printf("Ingrese %d enteros\n", longitud);
    int datos[MAX_LONGITUD];
    for (int i = 0; i < longitud; ++i) {
        if (scanf("%d", &datos[i]) != 1) {
            printf("Valor invalido\n");
            return 1;
        }
    }

    printf("Ingrese la cantidad de posiciones a rotar\n");
    int k;
    if (scanf("%d", &k) != 1 || k < 0 || k > longitud) {
        printf("Cantidad invalida\n");
        return 1;
    }

    rotar(datos, longitud, k);

    for (int i = 0; i < longitud; ++i) {
        printf("%d ", datos[i]);
    }
    printf("\n");
}



void revertir(int *arreglo, int longitud) {
    for (int i = 0; i < longitud/2; ++i) {
        int temp = arreglo[i];
        arreglo[i] = arreglo[longitud-i-1];
        arreglo[longitud-i-1] = temp;
    }
}

void rotar(int *arreglo, int longitud, int k) {
    revertir(arreglo, k);
    revertir(arreglo + k, longitud - k);
    revertir(arreglo, longitud);
}