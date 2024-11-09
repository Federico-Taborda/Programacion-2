#include <stdio.h>

void imprimir(int camas, char* planta){
    if (camas == 1)
        printf("Su habitacion tiene 1 cama y esta en la %s planta\n", planta);
    else 
        printf("Su habitacion tiene %d camas y esta en la %s planta\n", camas, planta);
}


int main(){
    int habitacion;
    
    printf("Habitaciones:\n\t1.Azul\n\t2.Roja\n\t3.Verde\n\t4.Rosa\n\t5.Gris\n\n");
    printf("Selecionar una habitacion: ");
    scanf("%d", &habitacion);

    switch (habitacion){
    case 1:
        imprimir(2, "primera");
        break;
    case 2:
        imprimir(1, "primera");
        break;
    case 3:
        imprimir(3, "segunda");
        break;
    case 4:
        imprimir(2, "segunda");
        break;
    case 5:
        imprimir(1, "tercera");
        break;
    default:
        printf("Numero no asociado a una habitacion\n");
        break;
    }
    return 0;
}