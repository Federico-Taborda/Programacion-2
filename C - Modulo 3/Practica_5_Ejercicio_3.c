#include<stdio.h>

void setin(int* n) {
    if(*n != 0) 
        *n = 1;
        else *n = 0;
}

int main() {
    int a = 20;
    int* p = &a;

    setin(p);

    printf("a:%d\n", a);

    return 0;
}