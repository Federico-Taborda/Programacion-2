def duplicado(lista):
    indice = 0

    while not indice == len(lista):
        if lista[indice] in lista[indice + 1:]:
            return True
        indice += 1

    return False

print(duplicado([1,2,3,4,4]))
print(duplicado(["a", "b", "c"]))
print(duplicado(["a", "a", "a"]))

def duplicado_recursivo(lista, nueva_lista = [], indice = 0):
    if indice == len(lista):
        return False
    
    if lista[indice] in nueva_lista:
        return True
    
    nueva_lista.append(lista[indice])

    return duplicado_recursivo(lista, nueva_lista, indice + 1)

print(duplicado_recursivo([1,2,3,4]))
print(duplicado_recursivo([1,2,3,4,4]))
print(duplicado_recursivo(["a", "a", "a"]))

