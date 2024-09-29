#include<stdio.h>

int main() {
    int a, b, c, d = 6, e;
    a = b = 3;
    c = a * b + d;
    e = (c + 5) / 4 - 3;
    e += 5;
    printf("Los resultados son %d y %d ", c, e);
    return 0;
}