#include<stdio.h>

int main() {
    int n, m;

    printf("Ingrese dos numeros\n");
    scanf("%d%d", &n, &m);

    if(n > m) {
        main();
    }

    while(n <= m) {
        printf("%d\n", n);
        n++;
    }

    return 0;
}