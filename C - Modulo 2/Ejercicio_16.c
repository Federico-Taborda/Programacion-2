#include<stdio.h>

int sumArr(int arr[], int longitud) {
    if(longitud == 1) return 1;

    if(longitud % 2 == 0) return arr[longitud - 1] * sumArr(arr, longitud - 1);

    return 1 * sumArr(arr, longitud - 1);
}

int main() {
    int longitud = 6;
    int producto;
    int arr[longitud];

    for(int i = 0; i < longitud; i++) {
        arr[i] = i;
    }

    producto = sumArr(arr, longitud);

    printf("%d", producto);
    
    return 0;
}
