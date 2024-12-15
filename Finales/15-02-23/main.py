from random import *

# La funcion carga los datos del archivo de salida del programa de C
# y devuelve un conjunto de tuplas que representa a una persona
def cargarDatos():
    personas = set()

    with open("./salida.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.split(',')
            personas.add((datos[0], datos[1], datos[2], int(datos[3])))
    
    return personas

# Dado un conjunto de personas, una edad minima y una edad maxima la funcion devuelve un conjunto de personas de min a max
def filtrarPersonasPorEdad(personas, min, max = 100):
    menores = set()

    for (nombre, apellido, localidad, edad) in personas:
        if min < edad < max:
            menores.add((nombre, apellido, localidad, edad))
    
    return menores

# Dado un conjunto de personas, un apellido y una localidad la funcion devuelve una lista de personas que
# no coincidan con el apellido dado pero si con la localidad dada
def personasCompatibles(personas, apellidoDado, localidadDada, edadDada):
    compatibles = set()
    menor = 12 < edadDada < 16
    mayor = edadDada > 16

    for (nombre, apellido, localidad, edad) in personas:
        if apellido != apellidoDado and localidad == localidadDada:
            compatibles.add((nombre, apellido, localidad, edad))
    
    # Si la persona es menor se quitaran las personas mayores
    if menor:
        compatibles = compatibles.difference(filtrarPersonasPorEdad(compatibles, 16))
    
    # Si la persona es mayor se quitaran los menores
    if mayor:
        compatibles = compatibles.difference(filtrarPersonasPorEdad(compatibles, 12, 16))

    return compatibles

# Dada una persona y un conjunto de personas la funcion devuelve un conjunto de dos personas
def unir(personas, persona):
    (nombre, apellido, localidad, edad) = persona
    opciones = list(personasCompatibles(personas, apellido, localidad, edad))

    if len(opciones) > 0:
        numeroRandom = randint(0, len(opciones) - 1)
        return (persona, opciones[numeroRandom])
    
    return set()

# La funcion toma un conjunto de parejas y las imprime en un archivo
def escribirDatos(personas):

    with open("file.txt", "a") as archivo:
        for pareja in personas:
            par = list(pareja)
            cadena = par[0][0] + "," + par[0][1] + ","  + par[1][0] + "," + par[1][1] + "\n"
            archivo.write(cadena)
    
    return personas

def main():
    personasDisponibles = cargarDatos()
    personasSolas = filtrarPersonasPorEdad(personasDisponibles, 0, 12)
    personasUnidas = set()

    # Quitamos a las personas menores de 12 de las disponibles
    personasDisponibles = personasDisponibles.difference(personasSolas)

    # Mientras haya personas disponibles se tratara unirlas
    while len(personasDisponibles) > 0:
        persona = list(personasDisponibles)[0]
        union = unir(personasDisponibles, persona) 

        if union:
            personasUnidas.add(union)
            personasDisponibles = personasDisponibles.difference(union)
        else:
            personasSolas.add(persona)
            personasDisponibles = personasDisponibles.difference({persona})

    # Escribe los datos en un archivo
    escribirDatos(personasUnidas)
    
    # Imprime las personas no emparejadas
    print("Las siguientes personas no pueden ser emparejadas")
    for persona in personasSolas:
        print(persona)
        
    

if __name__ == "__main__":
    main()