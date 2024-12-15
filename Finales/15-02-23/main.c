#include<stdio.h>
#include<string.h>
#include<stdlib.h>

// Informacion de cada persona
typedef struct {
    char *nombre;
    char *apellido;
    char *localidad;
    int edad;
} Persona;

void guardarDatos(Persona *personas, int cantidadPersonas);
Persona pedirDatos();
int buscarPersona(Persona *personas, int cantidadPersonas, Persona persona);
void liberarMemoria(Persona *personas, int cantidadPersonas);

int main() {
    int cantidadMaximaPersonas = 3;
    int cantidadPersonas = 0;
    Persona *personas;

    while (cantidadPersonas < cantidadMaximaPersonas) {
        Persona nuevaPersona;

        nuevaPersona = pedirDatos();

        // Si el array no tiene personas agrega la nueva persona
        if(cantidadPersonas == 0) {
            personas = malloc(sizeof(Persona));
            personas[0] = nuevaPersona;
        }else{
            // Si la nueva persona no esta en el array la agrega sino no
            if(!buscarPersona(personas, cantidadPersonas, nuevaPersona)) {
                personas = realloc(personas, sizeof(Persona) * (cantidadPersonas + 1));
                personas[cantidadPersonas] = nuevaPersona;
            }else{
                cantidadPersonas--;
            }
        }
        cantidadPersonas++;
    }

    guardarDatos(personas, cantidadPersonas);
    liberarMemoria(personas, cantidadPersonas);

    return 0;
}

// Dado un array de personas y la cantidad de personas que almacena 
// la funcion guarda los datos ingresados en un archivo
void guardarDatos(Persona *personas, int cantidadPersonas) {
    FILE *archivo;

    archivo = fopen("salida.txt", "a");

    for (int i = 0; i < cantidadPersonas; i++) {
        fprintf(archivo, "%s,%s,%s,%d\n", 
        personas[i].nombre, 
        personas[i].apellido, 
        personas[i].localidad, 
        personas[i].edad);
    }

    free(personas);
    
    fclose(archivo);
}

// La funcion pide datos al usuario y devuelve una estructura de tipo persona
Persona pedirDatos() {
    char temp[50];
    int edad;
    Persona persona;

    printf("Ingrese su nombre\n");
    scanf("%s", temp);
    persona.nombre = malloc(sizeof(char) * strlen(temp) + 1);
    strcpy(persona.nombre, temp);

    printf("Ingrese su apellido\n");
    scanf("%s", temp);
    persona.apellido = malloc(sizeof(char) * strlen(temp) + 1);
    strcpy(persona.apellido, temp);

    printf("Ingrese su localidad\n");
    scanf("%s", temp);
    persona.localidad = malloc(sizeof(char) * strlen(temp) + 1);
    strcpy(persona.localidad, temp);

    printf("Ingrese su edad\n");
    scanf("%d", &edad);
    persona.edad = edad;

    return persona;
}

// Dado un array de personas, la cantidad de personas que almacena y una persona a encontrar la funcion devuelve:
// 1 si la persona se encuentra en el array
// 0 si la persona no se encuentra en el array
int buscarPersona(Persona *personas, int cantidadPersonas, Persona persona) {
    int existe = 0;
    int i = 0;

    while (i < cantidadPersonas && !existe) {
        if(strcmp(personas[i].nombre, persona.nombre) == 0 && strcmp(personas[i].apellido, persona.apellido) == 0)
            existe = 1;
        i++;
    }
    
    return existe;
}

// Dado un array de personas la funcion libera la memoria pedida para los datos de cada persona
void liberarMemoria(Persona *personas, int cantidadPersonas) {
    for (int i = 0; i < cantidadPersonas; i++) {
        free(personas[i].nombre);
        free(personas[i].apellido);
        free(personas[i].localidad);
    }
}