#include<stdio.h>

int prodAlt(int arr[], int longitud) {
    if(longitud == 1) return 1;

    if(longitud % 2 == 0) return arr[longitud - 1] * prodAlt(arr, longitud - 1);

    return 1 * prodAlt(arr, longitud - 1);
}

int main() {
    int longitud = 6;
    int producto;
    int arr[longitud];

    for(int i = 0; i < longitud; i++) 
        arr[i] = i;

    producto = prodAlt(arr, longitud);

    printf("%d\n", producto);
    
    return 0;
}
