#include<stdio.h>

int main() {
    int enteros[100];
    int largo = 1;
    int apariciones = 0;
    int x;

    printf("Ingrese un numero entero: \n");
    scanf("%d", &enteros[largo]);

    while(enteros[largo] > 0) {
        largo++;
        printf("Ingrese un numero entero: \n");
        scanf("%d", &enteros[largo]);
    }

    for (int i = 0; i <= largo; i++) {
        int apariciones_dos = 0;
        for (int j = 0; j <= largo; j++) 
            if (enteros[i] == enteros[j]) 
                apariciones_dos++;
        

        if (apariciones < apariciones_dos) {
            x = enteros[i];
            apariciones = apariciones_dos;
        }
    }
    
    printf("%d\n", x);

    return 0;
}
