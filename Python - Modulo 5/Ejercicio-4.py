def grep(expresion, archivo):
    file = open(archivo, "r")

    for linea in file:
        if expresion in linea:
            print(linea)

    file.close()


grep("grep", "head.txt")