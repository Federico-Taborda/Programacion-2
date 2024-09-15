import math

def busqueda_dicotomica(lista, palabra):
    if lista == []:
        return False
    
    if len(lista) == 1 and not lista[0] == palabra:
        return False
    
    mitad = math.floor(len(lista) / 2)

    if palabra == lista[mitad]:
        return True
    
    if palabra < lista[mitad]:
        return busqueda_dicotomica(lista[:mitad], palabra)
    
    if palabra > lista[mitad]:
        return busqueda_dicotomica(lista[mitad:], palabra)
    
def test_busqueda_dicotomica():
    assert busqueda_dicotomica([], "a") == False
    assert busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "c") == True
    assert busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "e") == True
    assert busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "h") == True
    assert busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "i") == False