#include<stdio.h>
#include<math.h>

int sumatoria_a() {
    for (int i = 1; i < 100; i++) {
        printf("1/%d\n", i);
    }
    
    return 0;
}

int sumatoria_b() {
    for (int i = 1; i < 100; i++) {
        double k = pow(i, 2);
        printf("1/%.0f\n", k);
    }
    
    return 0;
}

int sumatoria_c() {
    for (int i = 1; i < 100; i++) {
        double k = pow(i, i);
        printf("1/%.0f\n", k);
    }
    
    return 0;
}

int sumatoria_d() {
    for (int i = 1; i < 100; i++) {
        int j = (i + 1) * i;
        printf("1/%d\n", j);
    }
    
    return 0;
}

int main() {
    //sumatoria_a();
    //sumatoria_b();
    //sumatoria_c();
    //sumatoria_d();
    return 0;
}