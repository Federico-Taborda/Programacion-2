#include<stdio.h>

int main() {
    int n, suma = 0;

    printf("Ingrese un numero entero entre 5 y 100\n");
    scanf("%d", &n);

    if(n < 5 || n > 100) {
        printf("Error\n");
        return 1;
    }

    int numeros[n];

    printf("Ingrese %d numeros enteros: \n", n);

    for (int i = 0; i < n; i++) {
        scanf("%d", &numeros[i]);
        suma += numeros[i];
    }

    if(suma > 30) 
        printf("%d es mayor a 30\n", suma);
    

    printf("%d es menor a 30\n", suma);

    return 0;
}
