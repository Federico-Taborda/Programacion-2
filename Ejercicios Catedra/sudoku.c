#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define N 3
#define LADO (N*N)
#define CANTIDAD_CASILLAS (LADO*LADO)

int celdas[CANTIDAD_CASILLAS];

int celda(int f, int c) {
	return f * LADO + c;
}

int celda_en_fila(int fila, int i) {
	return celda(fila, i);
}

int celda_en_columna(int columna, int i) {
	return celda(i, columna);
}

int celda_en_caja(int caja, int i) {
	int fc = caja / 3 * 3;
	int cc = caja % 3 * 3;
	return celda(fc + i/3, cc + i%3);
}

int es_valido() {

	for (int fila = 0; fila < LADO; ++fila) {
		for (int i = 0; i < LADO; ++i) {
			int ci = celda_en_fila(fila, i);
			for (int j = 0; j < i; ++j) {
				int cj = celda_en_fila(fila, j);
				if (celdas[ci] != 0 && celdas[cj] != 0 && celdas[ci] == celdas[cj]) {
					return 0;
				}
			}
		}
	}

	for (int column = 0; column < LADO; ++column) {
		for (int i = 0; i < LADO; ++i) {
			int ci = celda_en_columna(column, i);
			for (int j = 0; j < i; ++j) {
				int cj = celda_en_columna(column, j);
				if (celdas[ci] != 0 && celdas[cj] != 0 && celdas[ci] == celdas[cj]) {
					return 0;
				}
			}
		}
	}

	for (int caja = 0; caja < LADO; ++caja) {
		for (int i = 0; i < LADO; ++i) {
			int ci = celda_en_caja(caja, i);
			for (int j = 0; j < i; ++j) {
				int cj = celda_en_caja(caja, j);
				if (celdas[ci] != 0 && celdas[cj] != 0 && celdas[ci] == celdas[cj]) {
					return 0;
				}
			}
		}
	}

	return 1;
}


void mostrar_tablero() {
	for (int i = 0; i < LADO; ++i) {
		if (i != 0 && i%N == 0) {
			for (int j = 0; j < LADO; ++j) {
				if (j != 0 && j%N == 0) {
					printf("-|");
				}
				printf("--");
			}
			printf("\n");
		}
		for (int j = 0; j < LADO; ++j) {
			if (j != 0 && j%N == 0) {
				printf(" |");
			}
			int x = celdas[celda(i,j)];
			if (x == 0)
				printf(" _");
			else
				printf(" %d", x);
		}
		printf("\n");
	}
}


int resolver(int i) {
	//system("clear");
	//mostrar_tablero();

	//usleep(10000);
	// getchar();

	if (!es_valido()) return 0;
	if (i == CANTIDAD_CASILLAS) return 1;
	if (celdas[i] != 0) return resolver(i+1);
	for (int x = 1; x <= LADO; ++x) {
		celdas[i] = x;
		if (resolver(i+1)) return 1;
		celdas[i] = 0;
	}
	return 0;
}

int main(int argc, char **argv) {
	if (argc < 2) {
		printf("Uso: sudoku <archivo>\n");
		return 1;
	}

	char *ruta_archivo = argv[1];

	FILE* archivo = fopen(ruta_archivo, "r");
	if (archivo == NULL) {
		printf("El archivo no existe.\n");
		return 1;
	}
	
	char board[LADO][LADO+1];
	for (int i = 0; i < LADO; ++i) {
		fscanf(archivo, "%[^\n]%*c", board[i]);
	}

	fclose(archivo);

	for (int i = 0; i < LADO; ++i) {
		for (int j = 0; j < LADO; ++j) {
			celdas[celda(i, j)] = board[i][j] - '0';
		}
	}

	if (resolver(0)) {
		printf("SI\n");
		mostrar_tablero();
	} else {
		printf("NO\n");
	}
}
