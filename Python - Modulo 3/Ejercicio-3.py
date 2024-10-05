def elimina_uno(lista:list) -> list:
    nueva_lista = []
    for i in range(1, len(lista) - 1):
        nueva_lista.append(lista[i])
    
    return nueva_lista

def elimina_dos(lista:list) -> list: 
    return lista[1:len(lista) - 1]

# Esta opcion elimina el primer elemento de la lista fuera del ambito de la funcion
def elimina_tres(lista:list) -> list: 
    del lista[0]
    del lista[len(lista) - 1]
    return lista

# Esta opcion elimina el primer elemento de la lista dentro del ambito de la funcion
def elimina_cuatro(lista:list) -> list: 
    nueva_lista = []
    nueva_lista += lista

    del nueva_lista[0]
    del nueva_lista[len(nueva_lista) - 1]
    return nueva_lista


def test_elimina():
    assert elimina_uno([1,2,3]) == [2]  
    assert elimina_dos([1,2,3]) == [2]
    assert elimina_tres([1,2,3]) == [2]
    assert elimina_cuatro([1,2,3]) == [2]

