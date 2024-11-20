#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char *getnewline() {
    char temp[256];
    char *linea;

    printf("Ingrese una cadena\n");
    scanf("%[^\n]", temp);

    linea = temp;
    return linea;
}

int main() {
    char *p;
    p = getnewline();

    printf("%s\n", p);
    return 0;
}