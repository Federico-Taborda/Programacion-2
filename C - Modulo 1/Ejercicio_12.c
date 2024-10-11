#include<stdio.h>

int es_primo(int n) {
    if(n == 1) {
        return -1 ;
    }

    int cantidad_divisores = 0;
    int contador = 1;

    while(contador < n) {
        if(n % contador == 0) {
            cantidad_divisores++;
        }
        contador++;
    }

    return cantidad_divisores;
}

int main() {
    int numero_ingresado = 0;
    printf("Ingrese un numero\n");
    scanf("%d", &numero_ingresado);
    
    if(es_primo(numero_ingresado) > 2) {
        printf("No es primo\n");
    }else{
        printf("Es primo\n");
    }

    return 0;
}