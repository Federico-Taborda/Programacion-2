#include<stdio.h>
#include<string.h>

typedef struct  {
    char palo[10];
    int numero;
} Carta;

Carta azar(Carta[], int len) {
    
}

int main() {
    Carta mazo[48];

    for (int i = 0; i < 48; i++) {
        if (i < 12) {
            strcpy(mazo[i].palo, "Espadas");
        } else if (i < 24) {
            strcpy(mazo[i].palo, "Copas");
        } else if (i < 36) {
            strcpy(mazo[i].palo, "Oros");
        } else {
            strcpy(mazo[i].palo, "Bastos");
        }
        mazo[i].numero = (i % 12) + 1;  // Números de 1 a 12
    }
    
    return 0;
}
