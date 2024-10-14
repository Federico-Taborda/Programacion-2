def cantidad_elementos_distintos(lista:list) -> int:
    if lista == []:
        return 0
    
    nueva_lista = []

    for x in lista:
        if not x in nueva_lista:
            nueva_lista.append(x)
    
    return len(nueva_lista)

def cantidad_elementos_distintos_recursivo(lista:list, nueva_lista:list = [], indice:int = 0) -> int:
    if lista == []:
        return 0
    
    if indice >= len(lista):
        return len(nueva_lista)
    
    if not lista[indice] in nueva_lista:
        return cantidad_elementos_distintos_recursivo(lista, nueva_lista + [lista[indice]], indice + 1)

    return cantidad_elementos_distintos_recursivo(lista, nueva_lista, indice + 1)