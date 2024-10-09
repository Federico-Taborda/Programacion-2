#include<stdio.h>

int main() {
    int nota;

    printf("Ingrese una nota\n");
    scanf("%d", &nota);

    if(nota == 10) {
        printf("Sobresaliente\n");
    }else if(nota == 9) {
        printf("Distinguido\n");
    }else if(nota == 8) {
        printf("Muy bueno\n");
    }else if(nota == 7) {
        printf("Bueno\n");
    }else if(nota == 6) {
        printf("Aprobado\n");
    }else if(nota < 5 && nota > 2) {
        printf("Insuficiente\n");
    }else{
        printf("Nota invalida\n");
    }

    return 0;
}