#include<stdio.h>

int main() {
    int numero;

    printf("Ingrese un lado de un dado\n");
    scanf("%d", &numero);

    switch (numero) {
        case 1:
            printf("Lado opuesto: seis\n");
        break;
        
        case 2:
            printf("Lado opuesto: cinco\n");
        break;
        
        case 3:
            printf("Lado opuesto: cuatro\n");
        break;

        case 4:
            printf("Lado opuesto: tres\n");
        break;

        case 5:
            printf("Lado opuesto: dos\n");
        break;

        case 6:
            printf("Lado opuesto: uno\n");
        break;    

    default:
        printf("Numero incorrecto\n");
        break;
    }
    return 0;
}