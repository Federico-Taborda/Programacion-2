#include<stdio.h>
#include<string.h>

// Sin terminar

int main() {
    char cadena_ingresada[100];
    char caracter = 'a';
    int cantidadCaracteres = 0;

    printf("Ingrese una cadena\n");
    scanf("%[^\n]", cadena_ingresada);

    for (int i = 0; i < strlen(cadena_ingresada); i++) {
        int yaLoTengo = 0;

        while (!yaLoTengo) {
            if(cadena_ingresada[i] > caracter)
                caracter++;
                
            
            if(cadena_ingresada[i] == caracter) {
                cantidadCaracteres++;
                yaLoTengo = 1;
            }

            if(cadena_ingresada[i] < caracter) {
                caracter++;
                yaLoTengo = 1;
            }
            
        }
    }

    printf("%d\n", cantidadCaracteres);

    if(cantidadCaracteres == 26) {
        printf("%s es un pangrama\n", cadena_ingresada);
        return 0;
    }

    printf("%s no es un pangrama\n", cadena_ingresada);
        return 0;
}