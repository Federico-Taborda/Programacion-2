def mostrar_multiplos(n, m):
    for x in range(n, m):
        if x % n == 0: 
            print(x)

n = mostrar_multiplos(3, 30)

