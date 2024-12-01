#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef struct {
    int x;
    int y;
} Casilla;

typedef struct {
    char **matrizLaberinto;
    int dimension;
    int cantidadObstaculosAleatorios;
    int cantidadObstaculosFijos;
    Casilla *obstaculosAleatorios;
    Casilla *obstaculosFijos;
    Casilla posicionInicial;
    Casilla objetivo;
} Laberinto;

int inicializarLaberinto(Laberinto *laberinto, FILE *archivoEntrada) {
    char lineas[50];

    if (archivoEntrada == NULL) {
        printf("No se pudo abrir el archivo correctamente\n");
        return 1;
    }

    while (fgets(lineas, sizeof(lineas), archivoEntrada) != NULL) {
        lineas[strlen(lineas) - 1] = '\0';

        if(!strcmp(lineas, "dimension")) {
            fscanf(archivoEntrada, "%d", &laberinto->dimension);
        }

        if(!strcmp(lineas, "obstaculos fijos")) {
            Casilla obstaculo;

            while(strcmp(lineas, "obstaculos aleatorios")) {
                fscanf(archivoEntrada, "(%d,%d)", &obstaculo.x, &obstaculo.y);
                fgets(lineas, sizeof(lineas), archivoEntrada);
                lineas[strlen(lineas) - 1] = '\0';

                laberinto->obstaculosFijos[laberinto->cantidadObstaculosFijos].x = obstaculo.x;
                laberinto->obstaculosFijos[laberinto->cantidadObstaculosFijos].y = obstaculo.y;
                laberinto->cantidadObstaculosFijos++;
                laberinto->obstaculosFijos = realloc(laberinto->obstaculosFijos, sizeof(Casilla) * (laberinto->cantidadObstaculosFijos + 1));
            }
        }

        if(!strcmp(lineas, "obstaculos aleatorios")) {
            fscanf(archivoEntrada, "%d", &laberinto->cantidadObstaculosAleatorios);
        }

        if(!strcmp(lineas, "posicion inicial")) {
            fscanf(archivoEntrada, "(%d,%d)", &laberinto->posicionInicial.x, &laberinto->posicionInicial.y);
        }

        if(!strcmp(lineas, "objetivo")) {
            fscanf(archivoEntrada, "(%d,%d)", &laberinto->objetivo.x, &laberinto->objetivo.y);
        }
    }

    return 0;
}

void inicializarMatriz(Laberinto *laberinto) {
    laberinto->matrizLaberinto = malloc(sizeof(char *) * laberinto->dimension);

    // Inicializamos todas las casillas como vacias
    for (int i = 0; i < laberinto->dimension; i++) {
        laberinto->matrizLaberinto[i] = malloc(sizeof(char) * laberinto->dimension); 

        for (int j = 0; j < laberinto->dimension; j++) {
            laberinto->matrizLaberinto[i][j] = '0';
        }
    }

    // Inicializamos las casillas de salidas y llegada
    laberinto->matrizLaberinto[laberinto->posicionInicial.x][laberinto->posicionInicial.y] = '|';
    laberinto->matrizLaberinto[laberinto->objetivo.x][laberinto->objetivo.y] = 'X';

    // Inicializamos los obstaculos fijos
    for (int i = 0; i < laberinto->cantidadObstaculosFijos; i++) {
        int x = laberinto->obstaculosFijos[i].x;
        int y = laberinto->obstaculosFijos[i].y;
        laberinto->matrizLaberinto[x][y] = '1';
    }
}

int main() {
    Laberinto laberinto;
    laberinto.cantidadObstaculosFijos = 0;
    laberinto.obstaculosFijos = malloc(sizeof(Casilla));

    FILE *archivoEntrada = fopen("./entrada-C.txt", "r");

    inicializarLaberinto(&laberinto, archivoEntrada);
    inicializarMatriz(&laberinto);



        // Imprime por pantalla los datos del laberinto

    /* printf("Dimension: %d\n", laberinto.dimension);
    printf("Obstaculos Fijos:\n");
    for (int i = 0; i < laberinto.cantidadObstaculosFijos; i++) {
        printf("(%d, %d)\n", laberinto.obstaculosFijos[i].x, laberinto.obstaculosFijos[i].y);
    }
    printf("Obstaculos Aleatorios: %d\n", laberinto.obstaculosAleatorios);
    printf("Posicion Inicial: (%d, %d)\n", laberinto.posicionInicial.x, laberinto.posicionInicial.y);
    printf("Objetivo: (%d, %d)\n", laberinto.objetivo.x, laberinto.objetivo.y); */
    for (int i = 0; i < laberinto.dimension; i++) {
        for (int j = 0; j < laberinto.dimension; j++) {
            printf("%c", laberinto.matrizLaberinto[i][j]);
        }
        printf("\n");
    }
    


    fclose(archivoEntrada);
    free(laberinto.obstaculosFijos);
    free(laberinto.matrizLaberinto);
    return 0;
}