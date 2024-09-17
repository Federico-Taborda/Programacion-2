def elimina_duplicado_for(lista):
    nueva_lista = []

    for x in lista:
        if not x in nueva_lista:
            nueva_lista.append(x)
    
    return nueva_lista

def elimina_duplicado_dos(lista):
    if lista == []:
        return []
    lista.sort()
    nueva_lista = [lista[0]]

    for index in range(1, len(lista)):
        if lista[index] != lista[index - 1]:
            nueva_lista.append(lista[index])
    
    return nueva_lista

def elimina_duplicado_recursivo(lista, nueva_lista = [], index = 0):
    if index == len(lista):
        return nueva_lista
    
    if not lista[index] in nueva_lista:
        nueva_lista.append(lista[index])
        
    return elimina_duplicado_recursivo(lista, nueva_lista, index + 1)

def elimina_duplicado_conjuntos(lista):
    return list(set(lista))
    
def test_elimina_duplicado():
    assert elimina_duplicado_for([]) == []
    assert elimina_duplicado_for(["a", "a", "b"]) == ["a", "b"]
    assert elimina_duplicado_for([1, 1, 1]) == [1]
    assert elimina_duplicado_dos([]) == []
    assert elimina_duplicado_dos(["a", "a", "b"]) == ["a", "b"]
    assert elimina_duplicado_dos([1, 1, 1]) == [1]
    assert elimina_duplicado_recursivo([]) == []
    #assert elimina_duplicado_recursivo(["a", "a", "b"]) == ["a", "b"]
    assert elimina_duplicado_recursivo([1, 1, 1]) == [1]
    assert elimina_duplicado_conjuntos([]) == []
    assert elimina_duplicado_conjuntos(["a", "a", "b"]) == ["a", "b"]
    assert elimina_duplicado_conjuntos([1, 1, 1]) == [1]
