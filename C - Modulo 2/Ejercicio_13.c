#include<stdio.h>

int main() {
    int n;
    int suma = 0;

    printf("Ingrese un numero entero entre 5 y 100: \n");
    scanf("%d", &n);

    // Verificamos que el entero dado este en el rango deseado
    if(n < 5 || n > 100) {
        printf("Error");
        return 0;
    }

    printf("Ingrese %d numeros enteros: \n", n);

    int arr[n];
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    for (int i = 0; i < n; i++) {
        suma += arr[i];
    }

    if(suma > 30) {
        printf("%d es mayor a 30\n", suma);
    }else{
        printf("%d es menor a 30\n", suma);
    }
    
    return 0;
}
