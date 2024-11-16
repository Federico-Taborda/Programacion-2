#include<stdio.h>
#include<stdlib.h>


int main() {
    int *p = malloc(10);

    free(p);
    free(p);
    return 0;
}

/* 
El compilador detecta que se libera dos veces el espacio en memoria y
lanza un error de compilacion
*/
