#include<stdio.h>
#include<stdlib.h>

int main() {
    int *pi = malloc(sizeof(int));
    int *pj = malloc(sizeof(int));

    *pi = 11;
    pj = pi;

    printf("*p=%d, *pj=%d\n", *pi, *pj);
    free(pj);
    return 0;
}