def acumular_for(lista:list) -> list:
    nueva_lista = [lista[0]]
    
    for i in range(1, len(lista)):
        elemento_anterior =  nueva_lista[len(nueva_lista) - 1]
        nueva_lista.append(lista[i] + elemento_anterior)

    return nueva_lista

def acumular_while(lista:list) -> list:
    nueva_lista = [lista[0]]
    indice = 1

    while indice < len(lista):
        nueva_lista.append(nueva_lista[indice - 1] + lista[indice])
        indice += 1

    return nueva_lista

def acumular_recursivo(lista:list, i:int=1, nueva_lista:list = []) -> list:
    if i == len(lista):
        return nueva_lista
    
    if nueva_lista == []:
        nueva_lista.append(lista[0])
    
    elemento_anterior = nueva_lista[len(nueva_lista) - 1]
    elemento_actual = lista[i]
    nueva_lista.append(elemento_anterior + elemento_actual)

    return acumular_recursivo(lista, i + 1, nueva_lista)