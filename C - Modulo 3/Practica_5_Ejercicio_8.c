#include<stdio.h>
#include<stdlib.h>

typedef void (*VisitorFunc)(int);

int apply(int (*func)(int), int n) {
    return func(n);
}

void applyin(int (*func)(int), int *n) {
    *n = func(*n);
}

void recorre(VisitorFunc, int arr[], int len) {
    for (int i = 0; i < len; i++) {
        VisitorFunc(arr[i]);
    }
}

int sucesor(int n) {
    return n+1;
}

void imprimir(int n) {
    printf("%d\n", n);
}

int main() {
    int arr[3] = {1,2,3};
    int i = 2, resultado = 0;

    resultado = apply(sucesor, i);

    printf("Resultado: %d\n", resultado);

    applyin(sucesor, &i);
    recorre(imprimir, arr, 3);

    return 0;
}