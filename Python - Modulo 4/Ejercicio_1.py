# Ejercicio A
def apariciones(lista:list, elemento:any) -> int: 
    contador = 0

    for x in lista:
        if x == elemento:
            contador += 1

    return contador

def apariciones_recursivo(lista:list, elemento:any, indice:int = 0, contador:int = 0) -> int:
    if lista == []:
        return contador
    
    if indice >= len(lista):
        return contador
    
    if lista[indice] == elemento:
        contador += 1
    
    return apariciones_recursivo(lista, elemento, indice + 1, contador)

# Ejercicio B
def primera_coincidencia(lista:list, elemento:any)-> int:
    if lista == []:
        return -1

    indice = 0
    contador = 0

    while contador < 1:
        if lista[indice] == elemento:
            contador += 1
        else:
            indice += 1
    
    return indice

def primera_coincidencia_recursivo(lista: list, elemento:any, indice:int = 0) -> int:
    if lista == [] or indice >= len(lista):
        return -1
    
    if lista[indice] == elemento:
        return indice
    
    return primera_coincidencia_recursivo(lista, elemento, indice + 1)

# Ejercicio C
def lista_apariciones(lista:list, elemento:any)-> list: 
    if lista == []:
        return []
    
    posiciones = []
    indice = 0

    while indice < len(lista):
        if lista[indice] == elemento:
            posiciones.append(indice)
            indice += 1
        else:
            indice += 1

    return posiciones

def lista_apariciones_recursivo(lista:list, elemento:any, indice:int = 0, indices:list = []) -> list:
    if lista == []:
        return []
    
    if indice >= len(lista):
        return indices
    
    if lista[indice] == elemento:
        indices += [indice]
    
    return lista_apariciones_recursivo(lista, elemento, indice + 1, indices)
    