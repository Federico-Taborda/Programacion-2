def ordenada(lista:list) -> bool: 
    indice = 0

    while not indice + 1 == len(lista):

        if lista[indice] > lista[indice + 1]:
            return False

        indice += 1
    
    return True

def ordenada_recursiva(lista:list, i:int = 0) -> bool: 
    if i + 1 == len(lista):
        return True
    
    if lista[i] < lista[i + 1]:
        return ordenada_recursiva(lista, i + 1)
    
    return False