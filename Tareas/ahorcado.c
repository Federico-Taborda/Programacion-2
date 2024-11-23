#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef struct {
    char *palabra;
    int *secreto;
    int intentos;
    int aciertos;
    char codificacion;
} Ahorcado;

void pedirPalabra(Ahorcado *partida);
void generarSecreto(Ahorcado *partida);
void pedirCaracter(char *caracter);
void evaluar(Ahorcado *partida, char caracter);
void mostrarPalabra(Ahorcado *partida);

int main() {
    Ahorcado partida;
    partida.intentos = 7;
    partida.aciertos = 0;
    partida.codificacion = '_';
    pedirPalabra(&partida);
    generarSecreto(&partida);

    while (partida.aciertos < strlen(partida.palabra) && partida.intentos > 0) {
        char caracter;
        pedirCaracter(&caracter);
        evaluar(&partida, caracter);
    }

    if(partida.aciertos == strlen(partida.palabra) && partida.intentos > 0) 
        printf("Ganaste, la palabra es %s\n", partida.palabra);

    if(partida.intentos == 0)
        printf("Perdiste, la palabra es %s\n", partida.palabra);

    free(partida.palabra);
    free(partida.secreto);
    return 0;
}

void pedirPalabra(Ahorcado *partida) {
    char temp[40];
    
    printf("Ingrese una palabra\n");
    scanf(" %s", temp);

   partida->palabra = malloc(sizeof(char) * (strlen(temp) + 1));
    
    strcpy(partida->palabra, temp);;
}

void generarSecreto(Ahorcado *partida) {
    int largo = strlen(partida->palabra);
    partida->secreto = malloc(sizeof(int) * largo);

    for (int indice = 0; indice < largo; partida->secreto[indice++] = 0);
}

void pedirCaracter(char *caracter) {
    printf("Ingrese una caracter\n");
    scanf(" %c", caracter);
}

void evaluar(Ahorcado *partida, char caracter) {
    int largo = strlen(partida->palabra);
    int indice = 0;
    int contenida = 0;
    
    for (; indice < largo; indice++) {
        if(partida->palabra[indice] == caracter) {
            partida->secreto[indice] = 1;
            partida->aciertos++;
            contenida = 1;
        }
    }

    if(!contenida) {
        partida->intentos--;
        printf("El caracter '%c' no esta en la palabra: ", caracter);
    }else{
        printf("El caracter '%c' esta en la palabra: ", caracter);
    }

    mostrarPalabra(partida);
}

void mostrarPalabra(Ahorcado *partida) {
    int largo = strlen(partida->palabra);
    char *temp = malloc((largo + 1) * sizeof(char));

    for (int i = 0; i < largo; i++) {
        if (partida->secreto[i])
            temp[i] = partida->palabra[i];
        else
            temp[i] = partida->codificacion;
    }

    temp[largo] = '\0';

    printf("%s\n", temp);
}
