def posiciones_multiplo(lista:list, n:int) -> list:
    nueva_lista = []
    
    for x in lista:
        if x % n == 0:
            nueva_lista.append(lista.index(x))
    
    return nueva_lista

def posiciones_multiplo_recursiva(lista:list, n:int, i:int=0, nueva_lista:list = [])-> list:
    if i == len(lista):
        return nueva_lista
    
    if lista[i] % n == 0:
        nueva_lista.append(i)

    return posiciones_multiplo_recursiva(lista, n, i + 1, nueva_lista)

