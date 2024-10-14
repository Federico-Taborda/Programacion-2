# Ejercicio A
def valor_maximo_uno(lista:list) -> int:
    maximo = lista[0]

    for x in range(1, len(lista)):
        if lista[x] > maximo:
            maximo = lista[x]
    
    return maximo

# Ejercicio B
def valor_maximo_dos(lista:list) -> tuple:
    maximo = lista[0]
    indice = 0

    for x in range(1, len(lista)):
        if lista[x] > maximo:
            maximo = lista[x]
            indice = x
    
    return (maximo, indice)