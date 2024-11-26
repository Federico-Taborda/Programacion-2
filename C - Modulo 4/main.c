#include <stdio.h>
#include <stdlib.h>

// Dado un archivo y un entero n la funcion lee las primeras n lineas del archivo
void imprimir_n_lineas(FILE *archivo, int n) {
    char lineas[255];

    while (n > 0) {
        fgets(lineas, sizeof(lineas), archivo);
        printf("%s", lineas);
        n--;
    }
    
}

// Dados un archivo origen y uno destino la funcion copia el contenido de origen a destino
void copiar_contenido(FILE *origen, FILE *destino) {
    char lineas[255];

    while (fgets(lineas, sizeof(lineas), origen) != NULL) {
        fprintf(destino, "%s", lineas);
    }
}

int main() {
    //int lineas = 4;

    FILE *archivo_uno = fopen("./C - Modulo 4/test.txt", "r+");
    FILE *archivo_dos = fopen("./C - Modulo 4/test2.txt", "a+");

    //imprimir_n_lineas(archivo_uno, lineas);
    copiar_contenido(archivo_uno, archivo_dos);

    fclose(archivo_uno);
    fclose(archivo_dos);

    return 0;
}
