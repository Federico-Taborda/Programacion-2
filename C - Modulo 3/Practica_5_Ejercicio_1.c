#include<stdio.h>

int main() {
    int a, b, c;
    char abc[3] = {'a', 'b', 'c'};

    printf("a:%p b:%p c:%p\n", &a, &b, &c);
    printf("abc[0]:%p abc[1]:%p abc[2]:%p\n", &abc[0], &abc[1], &abc[2]);
    return 0;
}