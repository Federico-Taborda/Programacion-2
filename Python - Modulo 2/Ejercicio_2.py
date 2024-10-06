def imprimir_fichas(n:int, m:int) -> int:
    if n > 6:
        return

    ficha = n
    valor = m
    while valor <= 6:
        print(ficha, valor)
        valor += 1
    
    return imprimir_fichas(n + 1, m + 1)

#imprimir_fichas(0, 0)