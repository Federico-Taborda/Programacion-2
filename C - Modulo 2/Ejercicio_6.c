#include<stdio.h>
#define SECRETO 30

int main() {
    int numero;
    int intentos = 15;

    printf("Ingrese un numero entre 0 y 500\n");
    scanf("%d", &numero);

    for (int i = 0; i <= intentos; i++) {
        if(numero < SECRETO) {
            printf("El numero es mayor. Ingrese otro: \n");
            scanf("%d", &numero);
            intentos--;
        }else if (numero > SECRETO) {
            printf("El numero es menor. Ingrese otro: \n");
            scanf("%d", &numero);
            intentos--;
        }else{
            printf("Adivinaste\n");
            i = intentos;
        }
    }

    printf("Intentos maximos alcanzados\n");

    return 0;
}