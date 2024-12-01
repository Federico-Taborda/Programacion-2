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

int inicializarLaberinto(Laberinto *laberinto, FILE *archivoEntrada);
int coordenadaAleatoria(int n);
void crearObstaculosAleatorios(Laberinto *laberinto);
void colocarPosiciones(Laberinto *laberinto);
void colocarObstaculosFijos(Laberinto *laberinto);
void colocarObstaculosAleatorios(Laberinto *laberinto);
void inicializarMatriz(Laberinto *laberinto);
void imprimirLaberinto(Laberinto *laberinto);
void liberarLaberinto(Laberinto *laberinto);

int main() {
    srand(time(NULL));
    Laberinto laberinto;
    FILE *archivoEntrada = fopen("./entrada-C.txt", "r");

    inicializarLaberinto(&laberinto, archivoEntrada);
    inicializarMatriz(&laberinto);
    colocarPosiciones(&laberinto);
    colocarObstaculosFijos(&laberinto);
    crearObstaculosAleatorios(&laberinto);
    colocarObstaculosAleatorios(&laberinto);

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

// Dado un entero n la funcion devolvera un numero aleatorio de 0 a n - 1 
int coordenadaAleatoria(int n) {
    return rand() % n;
}

void crearObstaculosAleatorios(Laberinto *laberinto) {
    laberinto->obstaculosAleatorios = malloc(sizeof(Casilla) * laberinto->cantidadObstaculosAleatorios);

    for (int i = 0; i < laberinto->cantidadObstaculosAleatorios; i++) {
        Casilla obstaculoAleatorio;

        obstaculoAleatorio.x = coordenadaAleatoria(laberinto->dimension);
        obstaculoAleatorio.y = coordenadaAleatoria(laberinto->dimension);

        while(laberinto->matrizLaberinto[obstaculoAleatorio.x][obstaculoAleatorio.y] != '0') {
            obstaculoAleatorio.x = coordenadaAleatoria(laberinto->dimension);
            obstaculoAleatorio.y = coordenadaAleatoria(laberinto->dimension);
        }

        laberinto->obstaculosAleatorios[i] = obstaculoAleatorio;
    }
}

// Dado un laberinto coloca las posiciones de salida y llegada
void colocarPosiciones(Laberinto *laberinto) {
    laberinto->matrizLaberinto[laberinto->posicionInicial.x][laberinto->posicionInicial.y] = '|';
    laberinto->matrizLaberinto[laberinto->objetivo.x][laberinto->objetivo.y] = 'X';
}

// Dado un laberinto coloca los obstaculos fijos en la matriz
void colocarObstaculosFijos(Laberinto *laberinto) {
    for (int i = 0; i < laberinto->cantidadObstaculosFijos; i++) {
        int x = laberinto->obstaculosFijos[i].x;
        int y = laberinto->obstaculosFijos[i].y;
        laberinto->matrizLaberinto[x][y] = '1';
    }
}

// Dado un laberinto coloca los obstaculos aleatorios en la matriz
void colocarObstaculosAleatorios(Laberinto *laberinto) {
    for (int i = 0; i < laberinto->cantidadObstaculosAleatorios; i++) {
        int x = laberinto->obstaculosAleatorios[i].x;
        int y = laberinto->obstaculosAleatorios[i].y;
        laberinto->matrizLaberinto[x][y] = '1';
    }
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

// Dado un laberinto la funcion imprime la matriz del laberinto por consola
void imprimirLaberinto(Laberinto *laberinto) {
    for (int i = 0; i < laberinto->dimension; i++) {
        for (int j = 0; j < laberinto->dimension; j++) {
            printf("%c", laberinto->matrizLaberinto[i][j]);
        }
        printf("\n");
    }
}

// Dado un laberinto libera la memoria asignada dinamicamente
void liberarLaberinto(Laberinto *laberinto) {
    for (int i = 0; i < laberinto->dimension; i++)
        free(laberinto->matrizLaberinto[i]);
    free(laberinto->matrizLaberinto);
    free(laberinto->obstaculosFijos);
    free(laberinto->obstaculosAleatorios);
}