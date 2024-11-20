#include<stdio.h>

typedef struct {
    char *apellido;
    int anio_ingreso;
    char division;
} estudiante;

int main () {
    estudiante nuevo, *pest = &nuevo;
    nuevo.apellido = "Lopez";
    nuevo.anio_ingreso = 1998;
    nuevo.division = 'A';

    /*  
    a: nuevo->apellido 
    Es incorrecto porque el operador -> es para acceder a las propiedades de una 
    estructura referenciada por un puntero

    b: pest->division 
    Es correcto otra, forma seria (*pest)->apellido

    c: (*pest)->apellido 
    Es correcto, otra forma seria pest->division

    d: *pest->apellido+2
    Es correcto devuelve el primer caracter apellido sumado dos posiciones

    e: *(pest->apellido+2)
    Es correcto devuelve el primer caracter apellido sumado dos posiciones

    f: pest->apellido[2] Correcto 
    Es correcto devuelve el caracter de apellido en el indice 2
    */

    return 0;
}