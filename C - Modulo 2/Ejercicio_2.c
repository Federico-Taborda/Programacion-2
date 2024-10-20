#include<stdio.h>

int main() {
    int numero;

    printf("Habitacion Camas Planta\n");
    printf("1. Azul      2    Primera\n");
    printf("2. Roja      1    Primera\n");
    printf("3. Verde     3    Segunda\n");
    printf("4. Rosa      2    Segunda\n");
    printf("5. Gris      1    Tercera\n");

    printf("Elija una habitacion\n");
    scanf("%d", &numero);

    switch (numero) {
        case 1:
            printf("Primera planta 2 camas\n");
        break;
        
        case 2:
            printf("Primera planta 1 cama\n");
        break;
        
        case 3:
            printf("Segunda planta 3 camas\n");
        break;

        case 4:
            printf("Segunda planta 2 camas\n");
        break;

        case 5:
            printf("Tercera planta 1 cama\n");
        break;

    default:
        printf("Numero no asociado a habitacion\n");
        break;
    }
    return 0;
}