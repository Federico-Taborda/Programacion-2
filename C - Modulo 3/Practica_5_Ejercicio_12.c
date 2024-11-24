#include<stdio.h>
#include<string.h>
#include<stdlib.h>

// A: Definicion de estructura Contacto
typedef struct {
    char *nombre, *telefono;
    int edad;
} Contacto;

// D: Definicion de estructura Agenda
typedef struct {
    Contacto *contactos;
    int cantidadContactos;
} Agenda;

// B: Implementacion de crear contactos
Contacto crear_contactos() {
    Contacto nuevo_contacto;
    char temp[50];
    int edad;

    printf("<--Creando un contacto-->\n");

    printf("Ingrese su nombre: ");
    scanf("%s", temp);

    nuevo_contacto.nombre = malloc(sizeof(char) * strlen(temp) + 1);
    strcpy(nuevo_contacto.nombre, temp);

    printf("Ingrese un telefono: ");
    scanf("%s", temp);

    nuevo_contacto.telefono = malloc(sizeof(char) * strlen(temp) + 1);
    strcpy(nuevo_contacto.telefono, temp);

    printf("Ingrese su edad: ");
    scanf("%d", &edad);

    while (edad < 0) {
        printf("Edad invalida. Ingrese nuevamente su edad\n");
        scanf("%d", &edad);
    }

    nuevo_contacto.edad = edad;
    
    return nuevo_contacto;
}

// C: Implementacion de actualiza contacto
void actualizar_edad(Contacto *contacto) {
    int edad;

    printf("<--Actualizando la edad de %s-->\n", contacto->nombre);

    printf("Ingrese su edad: ");
    scanf("%d", &edad);

    while (edad < 0) {
        printf("Edad invalida. Ingrese nuevamente su edad\n");
        scanf(" %d\n", &edad);
    }

    contacto->edad = edad;
}

// E.1: Implementacion de dar de alta contacto
void alta_contacto(Agenda *agenda) {
    Contacto nuevo_contacto;

    nuevo_contacto = crear_contactos();

    if (agenda->cantidadContactos == 0) {
        agenda->contactos = malloc(sizeof(Contacto) * (agenda->cantidadContactos + 1));
    }else if (agenda->cantidadContactos > 0) {
        agenda->contactos = realloc(agenda->contactos, sizeof(Contacto) * (agenda->cantidadContactos + 1));  
    }
    
    agenda->contactos[agenda->cantidadContactos] = nuevo_contacto;
    agenda->cantidadContactos++;

    printf("<--Contacto %s agregado a la agenda-->\n", nuevo_contacto.nombre);
}

// E.2: Implementacion de modificar edad
void modificar_edad(Agenda *agenda) {
    char nombre[30];
    int i = 0, edad;

    printf("<--Ingrese el nombre del contacto a actualizar-->\n");

    printf("Ingrese un nombre: ");
    scanf("%s", nombre);

    while(i < agenda->cantidadContactos) {
        
        if(strcmp(agenda->contactos[i].nombre, nombre)) {
            printf("<--Actualizando la edad de %s-->\n", nombre);

            printf("Ingrese una edad: ");
            scanf("%d", &edad);

            agenda->contactos[i].edad = edad;
            i = agenda->cantidadContactos;
        }

        i++;
    }

    if (i == agenda->cantidadContactos) {
        printf("Contacto no encontrado\n");
    }else if (i > agenda->cantidadContactos) {
        printf("Edad modificada\n");
    }    
}

// E.3: Implementacion de imprimir contactos
void imprimir_contactos(Agenda *agenda) {
    printf("<--Imprimiendo todos los contactos-->\n");

    for (int i = 0; i < agenda->cantidadContactos; i++) {
        printf("nombre: %s - telefono: %s - edad: %d\n",
        agenda->contactos[i].nombre,
        agenda->contactos[i].telefono,
        agenda->contactos[i].edad);
    }
}

// F: Implementacion de promediar edades
double prom(Agenda *agenda) {
    int suma = 0;
    double promedio;

    printf("<--Calculando el promedio de edad de los contactos-->\n");

    for (int i = 0; i < agenda->cantidadContactos; i++) {
        suma += agenda->contactos[i].edad;
    }

    promedio = suma / agenda->cantidadContactos;
    return promedio;
}

int main() {
    // Creamos una agenda e inicializamos la cantidad de contactos en 0
    Agenda miAgenda;
    miAgenda.cantidadContactos = 0;

    // Creamos dos contactos
    alta_contacto(&miAgenda);
    alta_contacto(&miAgenda);

    // Actualizamos la edad del primer contacto
    actualizar_edad(&miAgenda.contactos[0]);

    // Actualizamos la edad de un contacto a partir de un nombre dado
    modificar_edad(&miAgenda);
    
    // Imprimimos cada contacto
    imprimir_contactos(&miAgenda);

    // Calculamos el promedio de edades de los contactos
    double promedio = prom(&miAgenda);
    printf("<--Promedio: %lf-->\n", promedio);

    return 0;
}