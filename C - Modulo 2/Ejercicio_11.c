#include<stdio.h>

int main() {
    int numeros[50];
    int i = 0;
    int j = 0;

    for (; i < 50; j++) {
        if(j % 3 == 0) {
            numeros[i] = j;
            i++;
        }
    }

    for (int j = 49; j >= 0; j--) 
        printf("%d: %d\n", j,numeros[j]);
    
    
    return 0;
}
