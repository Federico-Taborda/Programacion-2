#include <stdio.h>
#include <stdlib.h>




int pangrama_1(char* cadena) {
    int falta_letra = 0;
    for (char letra = 'a'; letra <= 'z' && !falta_letra; letra++) {
        int tengo_letra = 0;
        for (int i = 0; cadena[i] != '\0' && !tengo_letra; i++)
            if (cadena[i] == letra)
                tengo_letra = 1;
        if (!tengo_letra)
            falta_letra = 1;
    }
    return !falta_letra;
}

int pangrama_2(char* cadena) {
    char letras[26];
    int cantidad_letras_distintas = 0;
    for (int i = 0; cadena[i] != '\0' && cantidad_letras_distintas != 26; i++) {
        int ya_la_tengo = 0;
        for (int j = 0; j < cantidad_letras_distintas && !ya_la_tengo; j++)
            if (cadena[i] == letras[j])
                ya_la_tengo = 1;
        if (!ya_la_tengo)
            letras[cantidad_letras_distintas++] = cadena[i];
    }
    return cantidad_letras_distintas == 26;
}

int pangrama_3(char *cadena) {
    int letras[26] = {};
    int cantidad_letras = 0;
    for (int i = 0; cadena[i] != '\0'; i++) {
        int idx = cadena[i] % 26;
        if(letras[idx] == 0) { 
            letras[idx] = 1;
            cantidad_letras ++;
        }
    }    
    return cantidad_letras == 26;
}


int main(){
    
    char palabra[30];
    printf("Ingrese palabra: ");
    scanf("%s", palabra);

    printf("Pangrama1 = %d\n", pangrama_1(palabra));   
    printf("Pangrama2 = %d\n", pangrama_2(palabra));   
    printf("Pangrama3 = %d\n", pangrama_3(palabra));   
    return 0;
}