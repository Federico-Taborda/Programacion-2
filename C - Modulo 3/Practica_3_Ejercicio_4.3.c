#include<stdio.h>

int main() {
    int *ptr, a = 34;
    int b = 45;
    ptr = &b;
    *ptr = 34;
    printf("%d - %d\n", a, *ptr);
    return 0;
}