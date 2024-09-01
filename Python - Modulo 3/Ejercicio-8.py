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
    
print(busqueda_dicotomica([], "a"))
print(busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "c"))
print(busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "e"))
print(busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "h"))
print(busqueda_dicotomica(["a", "b", "c", "d", "e", "f", "g", "h"], "i"))