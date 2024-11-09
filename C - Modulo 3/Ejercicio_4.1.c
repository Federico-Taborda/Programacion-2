#include<stdio.h>


void initialize(int a, int b) {
    if (a > 0) b = 1; else b = 0;
}

int main() {
    int a, b;
    a = 1;
    initialize(a, b);
    printf("% d %d\n", a, b);
    return 0;
}