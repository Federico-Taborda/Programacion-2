def apariciones(lista, elemento): 
    contador = 0

    for x in lista:
        if x == elemento:
            contador += 1

    return contador

def primera_coincidencia(lista, elemento):
    indice = 0
    contador = 0

    while contador < 1:
        if lista[indice] == elemento:
            contador += 1
        else:
            indice += 1
    
    return indice

def lista_apariciones(lista, elemento): 
    posiciones = []
    indice = 0

    while indice < len(lista):
        if lista[indice] == elemento:
            posiciones.append(indice)
            indice += 1
        else:
            indice += 1

    return posiciones

print(lista_apariciones(["a", "a", "b", "a"], "a"))
    