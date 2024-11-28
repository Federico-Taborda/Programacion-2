#include<stdio.h>
#include<string.h>

int mayor(int vector[], int n) {
    int indice = 0;

    for (int i = 0; i < n; i++) {
        if(vector[i] > vector[indice]) {
            indice = i;
        }
    }
    
    return indice;
}

int masRepetido2(int vector[], int n) {
    int maxRepeticiones = 0, resultado = vector[0];

    for (int i = 0; i < n; i++) {
        int contador = 1;

        for (int j = i + 1; j < n; j++) {
            if (vector[i] == vector[j]) {
                contador++;
            }
        }

        if (contador > maxRepeticiones) {
            maxRepeticiones = contador;
            resultado = vector[i];
        }
    }

    return resultado;
}

int masRepetido(int vector[], int n) {
    int cantidadApariciones[n];
    int indice;

    for (int i = 0; i < n; i++) {
        int contadorApariciones = 1;
        for(int j = i + 1; j < n; j++) {
            if(vector[i] == vector[j]) {
                contadorApariciones++;
            }
        }

        cantidadApariciones[i] = contadorApariciones;
    }

    indice = mayor(cantidadApariciones, n);
    return vector[indice];
}

int reemplazarCaracter(char s[], char cviejo, char cnuevo) {
    int cantidadCambiados = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        if(s[i] == cviejo) {
            s[i] = cnuevo;
            cantidadCambiados++;
        }
    }

    return cantidadCambiados;
}

int main() {
    int numeros_uno[] = {22, 15, 7, 22, 15, 7, 22};
    int numeros_dos[] = {13, 5, 5, 5, 13, 9, 13};

    int resultado;
    
    resultado = masRepetido2(numeros_uno, 7);
    
    printf("%d\n", resultado);

    char s[256];
    int contador;
    char c1, c2;

    printf("Ingrese una cadena de caracteres\n");
    scanf(" %s", s);

    printf("Ingrese el caracter que desea reemplazar\n");
    scanf(" %c", &c1);

    printf("Ingrese el nuevo caracter\n");
    scanf(" %c", &c2);

    contador = reemplazarCaracter(s, c1, c2);

    printf("Cadena: %s - Cantidad cambiados: %d\n", s, contador);

    return 0;
}
