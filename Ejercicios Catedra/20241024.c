#include <stdio.h>

int fibonacci (int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacci(n-1) + fibonacci(n-2);
}


double factorial(int n){
    double factorial = 1;
    while (n > 1) {
        factorial *= n; // factorial = factorial * n;
        n--; // n = n-1;
    }    
    return factorial;
}


int fib_I (int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;

    int f_a2 = 0, f_a = 1, f_m = 1;
    int m = 2;
    while (m < n) {
        f_a2 = f_a;
        f_a = f_m;
        f_m = f_a + f_a2;
        m++;
    }

    return f_m;
}

int main () {
    int n = 0;
    while (n < 1) {
        printf("Ingrese un numero positivo: ");
        scanf("%d", &n);
    }


    //printf("%d! = %.0f\n", n, factorial(n));

    printf("fib iterativo %d = %d\n", n, fib_I(n));
    printf("fib recursivo %d = %d\n", n, fibonacci(n));

    return 0;
}
    // printf("fib_i %d = %d\n", n, fib_I(n));
    


