#include<stdio.h>
#include<string.h>

typedef struct  {
    int x, y;
} Punto;

Punto medio(Punto a, Punto b) {
    Punto p3;
    int x_m = (a.x + b.x ) / 2;
    int y_m = (a.y + b.y ) / 2;
    p3.x = x_m;
    p3.y = y_m;

    return p3;
}

int main() {
    Punto p1, p2, p3;
    p1.x = 2;
    p1.y = 3;
    p2.x = 6;
    p2.y = 5;

    p3 = medio(p1, p2);

    printf("Medio: (%d, %d)\n", p3.x, p3.y);
    
    return 0;
}
