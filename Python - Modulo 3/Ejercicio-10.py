def contar(l, cadena):
    contador = 0

    for x in cadena:
        if x == l:
            contador += 1
        
    return contador

print(contar("a", "palabra"))