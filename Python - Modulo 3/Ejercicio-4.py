def ordenada(lista):
    indice = 0

    while not indice + 1 == len(lista):

        if lista[indice] > lista[indice + 1]:
            return False

        indice += 1
    
    return True

def ordenada_recursiva(lista, i = 0):
    if i + 1 == len(lista):
        return True
    
    if lista[i] < lista[i + 1]:
        return ordenada_recursiva(lista, i + 1)
    
    return False

def test_ordenada():
    assert ordenada([1,2,3]) == True
    assert ordenada([4,2,3]) == False
    assert ordenada(["a", "b", "c"]) == True
    assert ordenada(["b", "a", "c"]) == False