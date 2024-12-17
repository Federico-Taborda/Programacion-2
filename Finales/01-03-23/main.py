from random import *

def cargarDatos():
    personas = set()

    with open("./salida.txt", "r") as archivo:
        for linea in archivo:
            datos = linea.split(',')
            personas.add((datos[0], datos[1], datos[2], int(datos[3])))
    
    return personas


def main():
    pass
        
    

if __name__ == "__main__":
    main()