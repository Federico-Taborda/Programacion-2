#include<stdio.h>
#include<math.h>

struct punto { double x; double y; } p1, p2;

double proyeccion(struct punto p, char eje) {
    return 0;
}

double distancia(struct punto p1, struct punto p2) {
    double dist;
    dist = sqrt(pow((p2.x - p1.x) , 2) + pow((p2.y - p1.y) , 2));
    return dist;
}

char cuadrante(struct punto p) {
    if(p.x == 0 && p.y == 0) return '0';
    if(p.x == 0) return 'y';
    if(p.y == 0) return 'x';
    if(p.x > 0 && p.y > 0) return '1';
    if(p.x < 0 && p.y > 0) return '2';
    if(p.x < 0 && p.y < 0) return '3';
    if(p.x > 0 && p.y < 0) return '4';
}

int main() {
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
