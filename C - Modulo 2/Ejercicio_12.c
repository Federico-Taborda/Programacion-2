#include<stdio.h>

int main() {
    int a[] = { 75, 64, 4, 95, 34, 56, 46, 85, 43, 24};
    int n = 56;

    for (int i = 0; i <= 9; i++) {
        if(a[i] == n) {
            printf("%d\n", i);
        }else{
            printf("%d\n", -1);
        }
    }
    
    return 0;
}
