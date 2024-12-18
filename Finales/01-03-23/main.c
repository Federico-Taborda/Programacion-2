#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>

// Estrucutura que representa a un barco y sus propiedades
typedef struct {
    int x;
    int y;
    int direccion;
    int tamaño;
} Barco;

// Estructura que reperesenta a un tablero y sus propiedades
typedef struct {
    int filas;
    int columnas;
    int cantidadBarcosAleatorios;
    Barco *barcos;
} Tablero;

int numeroAleatorio(int n, int m);
int validarBarco(Tablero tablero, Barco barco);
int barcosSuperpuestos(Barco barcoUno, Barco barcoDos);

int main() {
    srand(time(NULL));

    int dimesionMaxima = 20;
    int dimensionMinima = 10;
    int cantidadBarcosGuardados = 0;
    char lineas[60];
    Barco barcos[50];

    FILE *archivo;
    Tablero tablero;

    archivo = fopen("entrada.txt", "r");

    // Leer las dimensiones del tablero
    fscanf(archivo, "%d %d", &tablero.filas, &tablero.columnas);

    // Verifica las dimensiones del tablero
    /* if(tablero.filas < dimensionMinima || tablero.filas > dimesionMaxima || tablero.columnas > dimesionMaxima || tablero.columnas < dimensionMinima) {
        printf("El tablero no cuenta con las dimensiones requeridas\n");
        return 1;
    } */

    // Lee y guarda todos los barcos del archivo
    while(fgets(lineas, sizeof(lineas), archivo) != NULL) {
        Barco barco;
        fscanf(archivo, "%d %d %d %d", &barco.x, &barco.y, &barco.direccion, &barco.tamaño);
        barcos[cantidadBarcosGuardados] = barco;
        cantidadBarcosGuardados++;
    }

    for (int i = 0; i < cantidadBarcosGuardados; i++) {
        printf("%d %d %d %d \n", barcos[i].x, barcos[i].y, barcos[i].direccion, barcos[i].tamaño);
    }

    // Incializamos la cantidad de barcos aleatorios
    tablero.cantidadBarcosAleatorios = numeroAleatorio(tablero.filas / 3, tablero.columnas);

    // Inicializamos el tamaño del array de barcos aleatorio del tablero
    tablero.barcos = malloc(sizeof(Barco) * tablero.cantidadBarcosAleatorios);
    int indiceBarcosAleatorios = tablero.cantidadBarcosAleatorios - 1;
    
    // Se crea la cantidad de barcos aleatorios y lo guardamos en el tablero
    while (indiceBarcosAleatorios >= 0) {
        int i = numeroAleatorio(0, cantidadBarcosGuardados);

        // Si el barco es valido lo agregamos al tablero
        if(validarBarco(tablero, barcos[i])) {
            tablero.barcos[indiceBarcosAleatorios] = barcos[i];
            indiceBarcosAleatorios--;
        }
    }

    for (int i = 0; i < tablero.cantidadBarcosAleatorios; i++) {
        printf("x: %d y:%d direccion:%d largo:%d\n", tablero.barcos[i].x, tablero.barcos[i].y,  tablero.barcos[i].direccion, tablero.barcos[i].tamaño );
    }
    

    free(tablero.barcos);
    fclose(archivo);
    return 0;
}

void guardarDatos() {
    
}

// Dado un tablero y un barco la funcion devuelve 1 si el barco es valido
// para guardar en el tablero o 0 si no lo es
int validarBarco(Tablero tablero, Barco barco) {
    int coordenadaValida =  barco.x >= 0 && barco.x < tablero.filas && barco.y >= 0 && barco.y < tablero.columnas;
    int longitudValida = barco.tamaño >= 2 && barco.tamaño <= 4;
    int direccionValida = barco.direccion == 1 || barco.direccion == 0;
    int noPisaOtroBarco = 0;

    /* for (int i = 0; i < tablero.cantidadBarcosAleatorios; i++) {
        noPisaOtroBarco += barcosSuperpuestos(barco, tablero.barcos[i]);
    } */
    
    return coordenadaValida && longitudValida && direccionValida; /* && noPisaOtroBarco; */
}

// Dados dos barcos la funcion devuelve 1 si es los barcos tienen coordenadas
// superpuestas o 0 si no;
int barcosSuperpuestos(Barco barcoUno, Barco barcoDos) {
    int casillasSuperpuestas = 0;
    int x1 = barcoUno.x;
    int y1 = barcoUno.y;
    int x2 = barcoDos.x;
    int y2 = barcoDos.y;

    for (int i = 0; i < barcoUno.tamaño; i++) {
        for (int j = 0; j < barcoDos.tamaño; j++) {
            if (x1 == x2 && y1 == y2) {
                casillasSuperpuestas++;
            }
            
            if(barcoDos.direccion) {
                x2++;
            }else{
                y2++;
            }
        }

        if(barcoUno.direccion) {
            x1++;
        }else{
            y1++;
        }
    }
    
    return casillasSuperpuestas != 0; 
}

// Dado un numero entero positivo n la funcion devuelve un numero entre n y m
int numeroAleatorio(int n, int m) {
    return n + rand() % (m - n + 1);
}