#include <stdio.h>

int main() {
    int a, b, c;
    
    for (a = 1; a <= 20; a++) {
        for (b = 1; b <= 30; b++) {
            c = a * a + b * b;
            
            int c_int = (int)sqrt(c);
            if (c_int * c_int == c) 
                printf("(%d, %d, %d)\n", a, b, c_int);
            
        }
    }

    return 0;
}