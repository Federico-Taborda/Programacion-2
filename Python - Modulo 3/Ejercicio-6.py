def elimina_duplicado(lista):
    nueva_lista = []

    for x in lista:
        if not x in nueva_lista:
            nueva_lista.append(x)
    
    return nueva_lista

def test_elimina_duplicado():
    assert elimina_duplicado([]) == []
    assert elimina_duplicado(["a", "a", "b"]) == ["a", "b"]
    assert elimina_duplicado([1, 1, 1]) == [1]

def elimina_duplicado_recursivo(lista, nueva_lista = [], index = 0):
    if lista == []:
        return nueva_lista
    
    if not lista[index] in nueva_lista:
        nueva_lista.append(lista[index])
        return elimina_duplicado_recursivo(lista, nueva_lista, index + 1)