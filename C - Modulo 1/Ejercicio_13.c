#include<stdio.h>

int factorial(int n) {
    if(n == 0) 
        return 1;

    return n * factorial(n - 1);
}

int ejercicio_13() {
    int aux;
    int numero;
    // usar un int no sirve si el numero es muy grande
    // double factorial = 1;
    // while n > 1
        // factorial *= n
        // n--
    // %.0f muestra un double por pantalla sin decimales
    printf("Ingrese un numero positivo\n");
    scanf("%d", &numero);

    while (numero < 0) {
        printf("El numero no debe ser negativo. Ingrese un numero positivo\n");
        scanf("%d", &numero);
    }
    
    if(numero > 0) {
        aux = factorial(numero);
        printf("%d\n", aux);
    }else{
        printf("El numero ingresado no es positivo\n");
    }

    return 0; 
}

int main() {
    int a = 0;
    int b = 0;

    printf("Ingrese un numero\n");
    scanf("%d", &a);

    b = factorial(a);

    printf("El factorial de %d es %d", a, b);
    return 0;
}