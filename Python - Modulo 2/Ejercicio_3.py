def imprimir_fichas(n:int, m:int, delta:int) -> int:
    if n > delta:
        return

    ficha = n
    valor = m
    while valor <= delta:
        print(ficha, valor)
        valor += 1
    
    return imprimir_fichas(n + 1, m + 1, delta)

#imprimir_fichas(0, 0, 10)