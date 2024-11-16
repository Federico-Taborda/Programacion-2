#include <stdio.h>

int main() {
    int x, y;

    printf ("Ingrese dos enteros dentro del rango [1 ,20]:\n");
    scanf(" %d %d", &x, &y);

    if (x >=1 && y>=1 && x<=20 && y<=20) {
        for (int i=1; i<=y; i++) {
            for (int j=1; j<=x; j++)
                printf ("@");
            
            printf ("\n");
        }
    } else {
        printf("Los enteros no se encuentran en el rango pedido");
    }

    return 0;
}

// Imprime "x" cantidad de @ cada "y" cantidad de saltos de linea