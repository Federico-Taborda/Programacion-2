#include<stdio.h>

int main() {
    int temperatura;
    printf("Introduzca una temperatura:\n");
    scanf("%d", &temperatura);
    
    if(temperatura < 0) {
        printf("Estado solido\n");
    }else if(temperatura > 0 && temperatura < 100) {
        printf("Estado liquido\n");
    }else if(temperatura > 100){
        printf("Estado gaseoso\n");
    }
    return 0;
}