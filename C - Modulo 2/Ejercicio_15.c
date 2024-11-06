#include<stdio.h>

int sumArr(int arr[], int longitud) {
    if(longitud == 0) return 0;

    return arr[longitud - 1] + sumArr(arr, longitud - 1);
}

int main() {
    int longitud = 5;
    int suma;
    int arr[longitud];

    for(int i = 0; i < longitud; i++) {
        arr[i] = i;
    }

    suma = sumArr(arr, longitud);

    printf("%d\n", suma);
    
    return 0;
}
