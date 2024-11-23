#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char *getnewline() {
    char temp[256];
    char *linea;

    printf("Ingrese una cadena\n");
    scanf("%[^\n]", temp);

    linea = malloc(sizeof(char) * (strlen(temp) + 1));
    strcpy(linea, temp);
    return linea;
}

int main() {
    char *p;
    p = getnewline();

    printf("%s\n", p);
    
    free(p);
    return 0;
}