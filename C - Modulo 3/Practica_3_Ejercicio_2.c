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

/*
a = tipo:(int) valor:3
&a = tipo:(int*) valor:direccion de memoria
*ptr = tipo:(int) valor:3
ptr = tipo:(int*) valor:direccion de memoria
&ptr = tipo:(int*) valor:direccion de memoria

qtr = tipo:(int*) valor:10
*qtr = tipo:(int) valor:10
vector = tipo:(int*) valor:direccion de memoria
&vector = tipo:(int*) valor:direccion de memoria
*vector = tipo:(int) valor:10

++qtr = tipo:(int*) valor:direccion de memoria
++*qtr = tipo:(int) valor:11
++*vector = tipo:(int) valor:11
*&ptr = tipo:(int*) valor:direccion de memoria
*/