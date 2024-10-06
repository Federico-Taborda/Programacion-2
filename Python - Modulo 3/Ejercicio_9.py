def mostrar_caracteres(palabra:str, arr:list = []) -> list:
    if palabra == palabra[0]:
        arr.append(palabra)
        return arr

    arr.append(palabra[-1])
    return mostrar_caracteres(palabra[:-1], arr)

def mostrar_caracteres_for(palabra:str) -> list:
    arr = []
    for str in range(1, len(palabra) + 1):
        arr.append(palabra[-str])

    return arr

def mostrar_caracteres_while(palabra:str) -> list:
    arr = []
    indice = 1

    while indice < len(palabra) + 1:
        arr.append(palabra[-indice])
        indice += 1
    
    return arr

def mostrar_caracteres_recursivo(palabra:str, index:int = -1, arr:list = []) -> list:
    if abs(index) == len(palabra) + 1:
        return arr
    
    arr.append(palabra[index])
    return mostrar_caracteres_recursivo(palabra, index - 1, arr)
