def elimina_duplicado_for(lista:list) -> list: 
    nueva_lista = []

    for x in lista:
        if not x in nueva_lista:
            nueva_lista.append(x)
    
    return nueva_lista

def elimina_duplicado_dos(lista:list) -> list: 
    if lista == []:
        return []
    lista.sort()
    nueva_lista = [lista[0]]

    for index in range(1, len(lista)):
        if lista[index] != lista[index - 1]:
            nueva_lista.append(lista[index])
    
    return nueva_lista

def elimina_duplicado_recursivo(lista:list, nueva_lista:list = [], index:int = 0)-> list: 
    if index == len(lista):
        return nueva_lista
    
    if not lista[index] in nueva_lista:
        nueva_lista.append(lista[index])
        
    return elimina_duplicado_recursivo(lista, nueva_lista, index + 1)

def elimina_duplicado_conjuntos(lista:list) -> set:
    return list(set(lista))