def valor_maximo(lista:list) -> tuple:
    maximo = lista[0]
    indice = 0

    for x in range(1, len(lista)):
        if lista[x] > maximo:
            maximo = lista[x]
            indice = x
    
    return (maximo, indice)

#print(valor_maximo([3,4,7,2,5,1,3,5,8,11,2,55]))
#print(valor_maximo(["f", "h", "a", "i", "r", "s"]))