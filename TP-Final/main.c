#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include <time.h>

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

int coordenadaAleatoria(int n);
int inicializarLaberinto(Laberinto *laberinto, FILE *archivoEntrada);
void inicializarMatriz(Laberinto *laberinto);
void crearObstaculosAleatorios(Laberinto *laberinto);
void colocarPosiciones(char **matrizLaberinto, Casilla posicionInicial, Casilla posicionObjetivo);
void colocarObstaculos(char **matrizLaberinto, Casilla obstaculos[], int cantidadObstaculos);
void imprimirLaberinto(Laberinto *laberinto);
void liberarLaberinto(Laberinto *laberinto);

int main() {
    srand(time(NULL));
    Laberinto laberinto;
    FILE *archivoEntrada = fopen("./EntradaLaberinto.txt", "r");

    inicializarLaberinto(&laberinto, archivoEntrada);
    inicializarMatriz(&laberinto);
    colocarPosiciones(laberinto.matrizLaberinto, laberinto.posicionInicial, laberinto.objetivo);
    crearObstaculosAleatorios(&laberinto);
    colocarObstaculos(laberinto.matrizLaberinto, laberinto.obstaculosFijos, laberinto.cantidadObstaculosFijos);
    colocarObstaculos(laberinto.matrizLaberinto, laberinto.obstaculosAleatorios, laberinto.cantidadObstaculosAleatorios);

    imprimirLaberinto(&laberinto);
    
    liberarLaberinto(&laberinto);
    return 0;
}

// Dado un laberinto y un archivo de entrada la funcion inicializa los datos del laberinto
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
            laberinto->cantidadObstaculosFijos = 0;
            laberinto->obstaculosFijos = malloc(sizeof(Casilla));

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

    fclose(archivoEntrada);

    return 0;
}

// Dado un laberinto inicializa las dimensiones de la matriz
void inicializarMatriz(Laberinto *laberinto) {
    laberinto->matrizLaberinto = malloc(sizeof(char *) * laberinto->dimension);

    // Inicializamos todas las casillas como vacias
    for (int i = 0; i < laberinto->dimension; i++) {
        laberinto->matrizLaberinto[i] = malloc(sizeof(char) * laberinto->dimension); 

        for (int j = 0; j < laberinto->dimension; j++) {
            laberinto->matrizLaberinto[i][j] = '0';
        }
    }
}

// Dado un entero n la funcion devolvera un numero aleatorio entre 0 y n 
int coordenadaAleatoria(int n) {
    return 1 + rand() % n;
}

// Dado un laberinto la funcion crea obstaculos aleatorios dentro de las dimensiones del tablero en casillas no ocupadas
void crearObstaculosAleatorios(Laberinto *laberinto) {
    laberinto->obstaculosAleatorios = malloc(sizeof(Casilla) * laberinto->cantidadObstaculosAleatorios);

    for (int i = 0; i < laberinto->cantidadObstaculosAleatorios; i++) {
        Casilla obstaculoAleatorio;

        obstaculoAleatorio.x = coordenadaAleatoria(laberinto->dimension);
        obstaculoAleatorio.y = coordenadaAleatoria(laberinto->dimension);

        // Si la casilla en las coordenadas (x,y) esta ocupada genera otro par de coordenadas hasta encontrar una que no lo este
        while(laberinto->matrizLaberinto[obstaculoAleatorio.x - 1][obstaculoAleatorio.y - 1] != '0') {
            obstaculoAleatorio.x = coordenadaAleatoria(laberinto->dimension);
            obstaculoAleatorio.y = coordenadaAleatoria(laberinto->dimension);
        }

        laberinto->obstaculosAleatorios[i] = obstaculoAleatorio;
    }
}

// Dado una matriz de un laberinto, la posicion inicial y una posicion objetivo la funcion coloca ambas posiciones en la matriz
void colocarPosiciones(char **matrizLaberinto, Casilla posicionInicial, Casilla posicionObjetivo) {
    matrizLaberinto[posicionInicial.y - 1][posicionInicial.x - 1] = '|';    
    matrizLaberinto[posicionObjetivo.y - 1][posicionObjetivo.x - 1] = 'X';
}

// Dado una matriz de un laberinto, un array de obstaculos y la cantidad de los mismos la funcion coloca los obstaculos en la matriz
void colocarObstaculos(char **matrizLaberinto, Casilla obstaculos[], int cantidadObstaculos) {
    for (int i = 0; i < cantidadObstaculos; i++) {
        int x = obstaculos[i].x;
        int y = obstaculos[i].y;
        matrizLaberinto[x - 1][y - 1] = '1';
    }
}

// Dado un laberinto la funcion imprime la matriz del laberinto por consola
void imprimirLaberinto(Laberinto *laberinto) {
    for (int i = 0; i < laberinto->dimension; i++) {
        for (int j = 0; j < laberinto->dimension; j++) {
            printf("%c", laberinto->matrizLaberinto[i][j]);
        }
        printf("\n");
    }
}

// Dado un laberinto libera toda la memoria asignada dinamicamente
void liberarLaberinto(Laberinto *laberinto) {
    for (int i = 0; i < laberinto->dimension; i++)
        free(laberinto->matrizLaberinto[i]);
    free(laberinto->matrizLaberinto);
    free(laberinto->obstaculosFijos);
    free(laberinto->obstaculosAleatorios);
}