#include<stdio.h>

int main() {
    int edad, mes;

    printf("Ingrese su edad y su mes de nacimiento:\n");
    scanf("%d %d", &edad, &mes);

    if((edad >= 21 && mes == 3) || (edad <= 19 && mes == 4)) printf("Aries\n");
    if((edad >= 20 && mes == 4) || (edad <= 20 && mes == 5)) printf("Tauro\n");
    if((edad >= 21 && mes == 5) || (edad <= 21 && mes == 6)) printf("Geminis\n");
    if((edad >= 22 && mes == 6) || (edad <= 21 && mes == 7)) printf("Cancer\n");
    if((edad >= 22 && mes == 7) || (edad <= 21 && mes == 8)) printf("Leo\n");
    if((edad >= 22 && mes == 8) || (edad <= 22 && mes == 9)) printf("Virgo\n");
    if((edad >= 22 && mes == 9) || (edad <= 22 && mes == 10)) printf("Libra\n");
    if((edad >= 23 && mes == 10) || (edad <= 21 && mes == 11)) printf("Escorpio\n");
    if((edad >= 22 && mes == 11) || (edad <= 21 && mes == 12)) printf("Sagitario\n");
    if((edad >= 22 && mes == 12) || (edad <= 20 && mes == 1)) printf("Capricornio\n");
    if((edad >= 21 && mes == 1) || (edad <= 19 && mes == 2)) printf("Acuario\n");
    if((edad >= 20 && mes == 2) || (edad <= 20 && mes == 3)) printf("Piscis\n");

    return 0;
}