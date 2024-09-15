def acumular_for(lista):
    nueva_lista = [lista[0]]
    
    for i in range(1, len(lista)):
        elemento_anterior =  nueva_lista[len(nueva_lista) - 1]
        nueva_lista.append(lista[i] + elemento_anterior)

    return nueva_lista

def acumular_while(lista):
    nueva_lista = [lista[0]]
    indice = 1

    while indice < len(lista):
        nueva_lista.append(nueva_lista[indice - 1] + lista[indice])
        indice += 1

    return nueva_lista

def acumular_recursivo(lista, i=1, nueva_lista = []):
    if i == len(lista):
        return nueva_lista
    
    if nueva_lista == []:
        nueva_lista.append(lista[0])
    
    elemento_anterior = nueva_lista[len(nueva_lista) - 1]
    elemento_actual = lista[i]
    nueva_lista.append(elemento_anterior + elemento_actual)

    return acumular_recursivo(lista, i + 1, nueva_lista)

print(acumular_while([1,2,3]))

def test_acumular():
    assert acumular_for([1,2,3]) == [1,3,6]
    assert acumular_for([1,1,1]) == [1,2,3]
    assert acumular_while([1,2,3]) == [1,3,6]
    assert acumular_while([1,1,1]) == [1,2,3]

def test_acumular_recursivo():
    assert acumular_recursivo([1,2,3]) == [1,3,6]
