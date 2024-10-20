#include<stdio.h>

int main() {
    int numeros[50];

    for (int i = 200; i <= 200 && i >= 100; i--) {
        if(i % 2 == 0) {
            numeros[i] = i;
            printf("%d\n", numeros[i]);
        }
    }
    
    return 0;
}
