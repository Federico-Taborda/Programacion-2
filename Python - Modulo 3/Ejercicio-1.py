def posiciones_multiplo(lista, n):
    nueva_lista = []
    
    for x in lista:
        if x % n == 0:
            nueva_lista.append(lista.index(x))
    
    return nueva_lista

print(posiciones_multiplo([1,2,3,4,5,6,7],2))

def test_posiciones_multiplo():
    assert posiciones_multiplo([1,2,3,4,5,6,7],2) == [1, 3, 5]
    assert posiciones_multiplo([1,2,3,4,5,6,7],3) == [2, 5]