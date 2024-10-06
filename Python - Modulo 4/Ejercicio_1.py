def apariciones(lista:list, elemento:any) -> int: 
    contador = 0

    for x in lista:
        if x == elemento:
            contador += 1

    return contador

def primera_coincidencia(lista:list, elemento:any)-> int:
    indice = 0
    contador = 0

    while contador < 1:
        if lista[indice] == elemento:
            contador += 1
        else:
            indice += 1
    
    return indice

def lista_apariciones(lista:list, elemento:any)-> list: 
    posiciones = []
    indice = 0

    while indice < len(lista):
        if lista[indice] == elemento:
            posiciones.append(indice)
            indice += 1
        else:
            indice += 1

    return posiciones

#print(lista_apariciones(["a", "a", "b", "a"], "a"))
    