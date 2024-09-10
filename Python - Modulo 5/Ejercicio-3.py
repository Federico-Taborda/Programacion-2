def wc(archivo):
    lineas = contar_lineas(archivo)
    palabras = contar_palabras(archivo)
    caracteres = contar_caracteres(archivo)
    
    return {
        lineas,
        palabras,
        caracteres
    }

def contar_lineas(archivo):
    lines = 0
    file = open(archivo,  "r")

    for line in file:
        lines += 1

    file.close()

    return lines

def contar_palabras(archivo):
    file = open(archivo,  "r")
    contenido = file.read()
    words = contenido.split()
    file.close()

    return len(words)

def contar_caracteres(archivo):
    file = open(archivo,  "r")
    contenido = file.read()
    characters = len(contenido)
    file.close()

    return characters

print(wc("head.txt"))

