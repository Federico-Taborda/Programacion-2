#include<stdio.h>

// Cambiar un arreglo de 0 a k por k hasta l en el mismo orden
// [1, 2, 3, 4, 5, 6] => [4, 5, 6, 1, 2, 3]

void reverse(int arr[], int inicio, int final) {
    while (inicio < final) {
        int temp = arr[inicio];
        arr[inicio] = arr[final];
        arr[final] = temp;
        inicio++;
        final--;
    }
}

void rotate(int arr[], int n, int k) {
    if (k < 0 || k >= n) {
        printf("Valor de k inválido.\n");
        return;
    }

    // Invertir la primera parte [0..k]
    reverse(arr, 0, k);
    // Invertir la segunda parte [k+1..n-1]
    reverse(arr, k + 1, n - 1);
    // Invertir el arreglo completo [0..n-1]
    reverse(arr, 0, n - 1);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6};
    int n = 6;
    int k;
    
    printf("Ingrese un numero entero:");
    scanf("%d", &k);

    rotate(arr, n, k);

    printf("Arreglo rotado:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}