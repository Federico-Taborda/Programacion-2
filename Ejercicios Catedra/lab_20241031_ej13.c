#include <stdio.h>
#define SUMA_MINIMA 30


// Definicion de las funciones de los prototipos
void carga_arreglo(int* arreglo, int longitud) {

    int temp;

    for (int i = 0 ; i < longitud ; i++) {
        
        printf("Ingrese un valor: ");
        scanf("%d", &temp);
        arreglo[i] = temp;
    }
}

int sumar_arreglo(int*, int);

int main() {

    int tamArreglo; 
    
    printf("Ingrese un entero entre 5 y 100: ");
    scanf("%d", &tamArreglo);

    if (  tamArreglo < 5 ||  100 < tamArreglo ) {
        printf("Longitud incorrecta. Finalizando programa...\n");
        return 1;
    }
    
    int arreglo[tamArreglo];

    carga_arreglo(arreglo, tamArreglo);
    
    if (sumar_arreglo(arreglo, tamArreglo) > SUMA_MINIMA) 
        printf("La suma de los elementos es mayor que %d\n", SUMA_MINIMA);
    else
        printf("La suma de los elementos es menor o igual que %d\n", SUMA_MINIMA);
    
    
    return 0;
}


int sumar_arreglo(int* arreglo, int longitud) {
    
    int sumaElementos = 0;

    for (int i = 0 ; i < longitud ; i++) 
        sumaElementos = sumaElementos + arreglo[i];

    return sumaElementos;
}

