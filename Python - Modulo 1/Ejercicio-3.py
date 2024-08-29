def imprimir(n, m):
    if n == 0:
        return m
    else:
        if m % 2 == 0:
            print(m)
            return imprimir(n - 1, m + 1)
        else: 
            return imprimir(n, m + 1)

imprimir(5, 10)