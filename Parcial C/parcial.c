#include<stdio.h>
#include<string.h>

int subsecuencia(char s[], char t[]);

int elementosDistintos(char s[]);

int main() {
    char cadena_uno[] = "ol";
    char cadena_dos[] = "programacion";
    int resultado;

    //resultado = subsecuencia(cadena_uno, cadena_dos);
    resultado = elementosDistintos(cadena_dos);
    
    printf("%d\n", resultado);

    return 0;
}

int subsecuencia(char s[], char t[]) {
    int j = 0;
    for (int i = 0; i < strlen(t); i++) {
        if(s[j] == t[i]) 
            j++;
    }

    if(j == strlen(s))
        return 1;

    return 0;    
}

int elementosDistintos(char s[]) {
    int distintos = 0;
    for (int i = 0; i < strlen(s); i++) {
        int yaLoTengo = 0;
        for (int j = 0; j < i ; j++) {
            if(s[i] == s[j])
                yaLoTengo = 1;
        }

        if(!yaLoTengo)
            distintos++;
    }

    return distintos;
}