#include<stdio.h>
#include<math.h>

typedef struct { double x; double y; } Punto;

double proyeccion(Punto p, char eje) {
    if(eje == 'x') return 'y';
    if(eje == 'y') return 'x';
    return 0;
}

double distancia(Punto p1, Punto p2) {
    double dist;
    dist = sqrt(pow((p2.x - p1.x) , 2) + pow((p2.y - p1.y) , 2));
    return dist;
}

char cuadrante(Punto p) {

    if(p.x == 0) {
        if(p.y == 0) return 'o';
        return 'y';
    }

    if(p.y == 0) return 'x';

    if(p.x > 0) {
        if(p.y > 0) return '1';
        return '4';
    }

    if(p.x < 0) {
        if(p.y > 0) return '2';
        return '3';
    }
}

int main() {
    Punto p1;
    Punto p2;
    double proy, dist;
    char eje_x = 'x';
    char eje_y = 'y';
    char cuad;

    p1.x = 2;
    p1.y = 6;
    p2.x = -4;
    p2.y = 8;

    proy = proyeccion(p1, eje_x);
    dist = distancia(p1, p2);
    cuad = cuadrante(p1);

    printf("Proyeccion en el eje %c: %lf\n", eje_x, proy);
    proy = proyeccion(p1, eje_y);
    printf("Proyeccion en el eje %c: %lf\n", eje_y, proy);
    printf("Distancia: %lf\n", dist);
    printf("Posicion: %c\n", cuad);
    
    return 0;
}
