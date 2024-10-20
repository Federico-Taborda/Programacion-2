#include<stdio.h>
#include<math.h>

int sumatoria_uno() {
    for (int i = 1; i < 100; i++) {
        int j = 1 / i;
        printf("%d\n", j);
    }
    
    return 0;
}

int sumatoria_dos() {
    for (int i = 1; i < 100; i++) {
        double k = pow(i, 2);
        int j = 1 / k;
        printf("%d\n", j);
    }
    
    return 0;
}

int sumatoria_tres() {
    for (int i = 1; i < 100; i++) {
        double k = pow(i, i);
        int j = 1 / k;
        printf("%d\n", j);
    }
    
    return 0;
}

int sumatoria_cuatro() {
    for (int i = 1; i < 100; i++) {
        int j = (i + 1) * i;
        printf("%d\n", j);
    }
    
    return 0;
}

int main() {
    //sumatoria_uno();
    //sumatoria_dos();
    //sumatoria_tres();
    //sumatoria_cuatro();
    return 0;
}