def duplicado(lista:list) -> bool:
    indice = 0

    while not indice == len(lista):
        if lista[indice] in lista[indice + 1:]:
            return True
        indice += 1

    return False

def duplicado_recursivo(lista:list, nueva_lista:list = [], indice:int = 0) -> bool:
    if indice == len(lista):
        return False
    
    if lista[indice] in nueva_lista:
        return True
    
    nueva_lista.append(lista[indice])

    return duplicado_recursivo(lista, nueva_lista, indice + 1)
