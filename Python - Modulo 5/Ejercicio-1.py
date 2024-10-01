def head(archivo, n):
    f = open(archivo, "r")
    linea = f.readline()

    while not n == 0:
        print(linea)
        linea = f.readline()
        n -= 1
    
    f.close()

head("head.txt", 2)