#include<stdio.h>

int main() {
    int vector[5] = { 10, 20, 30, 40, 50};
    int a = 3;
    int *ptr = &a;
    int *qtr = vector;

    printf("%d %p %d %p\n", a, &a, *ptr, ptr);
    printf("%p %d %p %p\n", &ptr, *ptr, qtr, ptr);
    printf("%d %p %p %d\n", *qtr, vector, &vector, *vector);
    printf("%p %d %d %p\n", ++qtr, ++*qtr, ++*vector, *&ptr);

    return 0;
}