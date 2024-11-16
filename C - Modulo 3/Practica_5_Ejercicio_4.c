#include<stdio.h>
#include<stdlib.h>

void swap(int *p, int *q) {
    int *r = malloc(sizeof(int));
    *r = *p;
    *p = *q;
    *q = *r;
    free(r);
}

int main() {
    int a = 1, b = 2;

    printf("a:%d - b:%d\n", a, b);

    swap(&a, &b);

    printf("a:%d - b:%d\n", a, b);

    return 0;
}