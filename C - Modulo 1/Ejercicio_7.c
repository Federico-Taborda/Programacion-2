#include<stdio.h>

int main() {
    int año;

    printf("Ingrese un año\n");
    scanf("%d", &año);

    if(año % 400 == 0 || (año % 4 == 0 && año % 4 != 0)) {
        printf("Bisiesto\n");
    }else {
        printf("Bisiesto\n");
    }

    return 0;
}