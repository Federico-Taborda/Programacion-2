#include<stdio.h>

struct estudiante {
    char *apellido;
    int anio_ingreso;
    char division;
};

int main () {

    struct estudiante nuevo, *pest = &nuevo;
    nuevo.apellido = "Lopez";
    nuevo.anio_ingreso = 1998;
    nuevo.division = 'A';

    // a: nuevo->apellido Incorrecto porque nuevo no es un puntero
    // b: pest->division Correcto
    // c: (*pest)->apellido Incorrecto
    // d: *pest->apellido+2
    // e: *(pest->apellido+2)
    // f: pest->apellido[2] Correcto

    return 0;
}