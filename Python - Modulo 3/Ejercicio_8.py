def busqueda_dicotomica(lista:list, elemento:any) -> bool:
    if lista == []:
        return False
    
    if len(lista) == 1 and not lista[0] == elemento:
        return False
    
    mitad = len(lista) // 2

    if elemento == lista[mitad]:
        return True
    
    if elemento < lista[mitad]:
        return busqueda_dicotomica(lista[:mitad], elemento)
    
    if elemento > lista[mitad]:
        return busqueda_dicotomica(lista[mitad:], elemento)
    
def busqueda_dicotomica_dos(lista:list, elemento:any) -> bool:
    if lista == []:
        return False

    mitad = len(lista) // 2

    if elemento > lista[mitad]:
        return busqueda_dicotomica_dos(lista[mitad+1:], elemento)
    elif elemento < lista[mitad]:
        return busqueda_dicotomica_dos(lista[:mitad], elemento)
    
    return True

def busqueda_dicotomica_tres(lista:list, elemento:any, inicio:int = 0, final:int = 0):
    if inicio == final:
        return False

    inicio = 0
    final = len(lista)
    mitad = (inicio + final) // 2

    if elemento > lista[mitad]:
        return busqueda_dicotomica_tres(lista, elemento, mitad - 1, final)
    elif elemento < lista[mitad]:
        return busqueda_dicotomica_tres(lista, elemento, inicio, mitad)
    
    return True

def busqueda_dicotomica_while(lista:list, elemento:any) -> bool:
    mitad = len(lista) // 2

    while lista != [] and lista[mitad] != elemento:
        if elemento < lista[mitad]:
            lista = lista[:mitad]
        else:
            lista = lista[mitad+1:]

        mitad = len(lista) // 2
    
    return lista != []