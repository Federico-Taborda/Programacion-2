from math import *

def busqueda_binaria(lista, elemento):
    low = 0
    mid = ceil(len(lista) / 2)
    high = len(lista) - 1
    found = False
    index = 0
    
    while not found:
        if lista[low] == elemento:
            found = True
            index = low
        
        if lista[high] == elemento:
            found = True
            index = high
        
        if lista[mid] == elemento:
            found = True
            index = mid

        if lista[mid] > elemento:
            high = mid
            mid = high // 2
        else:
            low = mid + 1
            mid = mid + ((high - mid) // 2)
     
    return index

def test_busqueda_binaria():
    assert busqueda_binaria([1,2,3,4,5,6,7,8,9,10], 4) == 3
    assert busqueda_binaria(["a", "b", "c", "d", "e", "f"], "b") == 2
    