#include<stdio.h>

int main() {
    int *ip1, ip2;
    char ch, *cp;

    // Es una violacion de tipo porque se esta asignando una cadena a un puntero de tipo int
    // ip1 = "cadena de ejemplo";

    // Es una violacion de tipo porque no se puede obtener la direccion de memoria de un carater
    //cp = &'a';

    // Es una violacion de tipo porque se esta asignando un caracter a un puntero de tipo int
    // ip1 = '\0';

    // Es una violacion de tipo porque no se puede asignar un entero a una direccion de memoria
    // ip1 = ip2;

    // Es una violacion de tipo porque no se puede asignar un caracter a un puntero directamente
    // cp = '\0';

    return 0;
}