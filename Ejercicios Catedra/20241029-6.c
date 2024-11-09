#include <stdio.h>

#define SECRETO 0

int main(){

    int secreto;

    for(int intentos = 15; intentos && secreto != SECRETO; intentos--){
        
        printf("Introducir el secreto: ");
        scanf("%d", &secreto);

        if (secreto < SECRETO)
            printf("El numero es mayor\n");
        else if (SECRETO < secreto)
            printf("El numero es menor\n");
    }

    if (secreto == SECRETO)
        printf("Tenes el secreto =)\n");

    return 0;
}













// int main(){

//     int bandera = 1;

//     for(int intentos = 15; intentos && bandera; intentos--){
        
//         int secreto;
//         printf("Introducir el secreto: ");
//         scanf("%d", &secreto);

//         if (secreto < SECRETO)
//             printf("El numero es mayor\n");
//         else if (SECRETO < secreto)
//             printf("El numero es menor\n");
//         else
//             bandera = 0;

//     }

//     if (bandera)
//         printf("Tenes el secreto =)\n");

//     return 0;
// }
