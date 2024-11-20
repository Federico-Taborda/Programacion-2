#include<stdio.h>
#include<stdlib.h>

int vector [5] = {10, 20, 30, 40, 50};

#define SIZE 100

/* Informacion sobre la celda */
typedef struct {
   char nombre[SIZE]; // nombre de la celda
   int identificador; //número identificador
   float calidad; // calidad de la señal (entre 0 y 100)
   struct informacionOp* op; // puntero a una segunda estructura
} informacionCelda;

typedef struct {
    char nombre[SIZE]; // nombre del operador
    int prioridad; // prioridad de conexión
    int ultimaComprobacion; //fecha de la ultima comprobación
} informacionOp;

int main() {
    informacionCelda a;
    informacionCelda* b;

    printf("Tamanño informacionCelda: %ld\n", sizeof(a)); // Salida: 120
    printf("Tamanño informacionCelda: %ld\n", sizeof(b)); // Salida: 8

    return 0;
}

// A
/* 
Una variable de tipo struct informacionCelda ocupa 112 bytes en memoria
 */

// B
/* 
informacionCelda a; Ocupa 112 bytes en memoria
informacionCelda* b; Ocupa 4 bytes en memoria
 */

// C
/* 
Si una estructura informacionCelda esta almacenada en la posicion de memoria
100 entoces sus elementos tendran las siguientes direcciones
nombre: 200
indentificador: 204
calidad: 208
informacion* op: 212
 */


// D
/* 
1 struct informacionCelda c;
Se declara una variable c de tipo informacionCelda

2 struct informacionCelda* cptr = &c;
Se declara un puntero cptr de tipo informacionCelda y se guarda la direccion
de memoria de c en ella

3 struct informacionCelda d;
Se declara una variable d de tipo informacionCelda

4 struct informacionCelda* dptr = cptr; 
Se declara un puntero dptr de tipo informacionCelda y se guarda la direccion
de memoria de cptr en el
*/