def agregar_linea(archivo, linea):
    archivo = open(archivo, "a")
    archivo.write(linea)
    archivo.close()

def copy(archivo1, archivo2):
    archivo = open(archivo1, "r")

    for linea in archivo:
        print(linea)
        agregar_linea(archivo2, linea)
    
    archivo.close()

copy("cp1.txt", "cp2.txt")