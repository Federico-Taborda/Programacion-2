#include<stdio.h>

int main() {
    int edad;

    printf("Ingrese una edad\n");
    scanf("%d", &edad);
    
    if (edad >= 65) {
     printf ("Seguridad Social");
    }else if(edad <= 17) {
        printf ("Exento");
    }else{
        printf ("Imposible");
    }

    return 0;
}


