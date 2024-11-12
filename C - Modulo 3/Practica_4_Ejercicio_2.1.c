#include<stdio.h>

// No entiendo el problema
int main() {
    char textoA[30] = "Agarrate Catalina";
    char textoB[30] = "El Cuarteto de Nos";
    char* p = textoA;
    char* q = textoB;
    char a;
    printf("textoA: %s\ntextoB: %s\n", textoA, textoB);
    while (*p++ == *q++) a = a;
    printf("while(*p++ = *q++);\n");
    printf("textoA: %s\ntextoB: %s\n", textoA, textoB);
    return 0;
}