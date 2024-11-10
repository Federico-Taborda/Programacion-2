#include<stdio.h>

struct vector {
    float x, y;
};

struct vector *normal (struct vector v) {
    struct vector *ptr;
    ptr->x = v.x;
    ptr->y = v.y;
    return ptr;
};



