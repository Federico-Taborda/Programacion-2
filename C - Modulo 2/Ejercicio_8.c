#include<stdio.h>

int main() {
    int ingresado;
    int pasos = 0;

    printf("Ingrese un numero positivo\n");
    scanf("%d", &ingresado);

    while (ingresado < 1) {
        printf("El numero no puede ser negativo. Ingrese otro numero\n");
        scanf("%d", &ingresado);
    }

    for (; ingresado > 1; pasos++) {
        if(ingresado % 2 == 0) {
            ingresado /= 2;
        }else{
            ingresado = (ingresado * 3) + 1;
        }
        printf("El siguiente valor es %d\n", ingresado);
    }

    printf("Valor final %d, numero de pasos %d\n", ingresado, pasos);

    return 0;
}