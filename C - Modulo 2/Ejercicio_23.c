#include<stdio.h>
#include<string.h>

int contenido(char cadena_uno[], char cadena_dos[]) {
    int j = 0;

    for (int i = 0; i < strlen(cadena_uno); i++) {
        if(cadena_uno[i] != cadena_dos[j] && j < strlen(cadena_dos)) 
            j = 0;
        if(cadena_uno[i] == cadena_dos[j]) 
            j++;
    }

    if (j == strlen(cadena_dos)) 
        return 1;
    
    return 0;
}

int contenido_recursivo(char cadena_uno[], char cadena_dos[], int indice, int j) {
    if(cadena_uno[indice] == '\0') {
        if (j == strlen(cadena_dos)) 
            return 1;
        else 
            return 0;
    }
    
    if(cadena_uno[indice] != cadena_dos[j] && j < strlen(cadena_dos)) 
        j = 0;
    if(cadena_uno[indice] == cadena_dos[j])
        j++;
    
    return contenido_recursivo(cadena_uno, cadena_dos, indice + 1, j);
}

int main() {
    char cadena_uno[100];
    char cadena_dos[100];
    int resultado;

    printf("Ingrese una cadena:\n");
    scanf(" %[^\n]", cadena_uno);

    printf("Ingrese otra cadena:\n");
    scanf(" %[^\n]", cadena_dos);

    //resultado = contenido(cadena_uno, cadena_dos);
    resultado = contenido_recursivo(cadena_uno, cadena_dos, 0, 0);

    if(resultado) {
        printf("%s esta contenido en %s\n", cadena_dos, cadena_uno);
    }else{
        printf("%s no esta contenido en %s\n", cadena_dos, cadena_uno);
    }


    return 0;
}