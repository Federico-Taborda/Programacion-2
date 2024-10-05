# Escriba dos versiones de una funcion denominada mayor.
#  Una de ellas debe implementarse utilizando el ciclo while, mientras que la otra debe utilizar el ciclo for
# La funcion debe recibir como argumento una lista de numeros y devolver el mayor elemento de dicha lista.
#  En caso de que la lista este vacia, la funcion debe indicar que la lista no posee elementos

def mayor_while(lista):
    if lista == []:
        return "Lista vacia"
    
    elemento = lista[0]
    indice = 0

    while indice < len(lista):
        if lista[indice] > elemento:
            elemento = lista[indice]
        indice += 1
    
    return "El elemento mayor es " + str(elemento)

def mayor_for(lista):
    if lista == []:
        return "Lista vacia"
    
    elemento = lista[0]
    
    for indice in range(0, len(lista)):
        if lista[indice] > elemento:
            elemento = lista[indice]

    return "El elemento mayor es " + str(elemento)

def test_mayor():
    assert mayor_while([]) == "Lista vacia"
    assert mayor_while([1]) == "El elemento mayor es 1"
    assert mayor_while([1, 2]) == "El elemento mayor es 2"
    assert mayor_while([2, 1]) == "El elemento mayor es 2"
    assert mayor_while([2, 1, 3]) == "El elemento mayor es 3"
    assert mayor_for([]) == "Lista vacia"
    assert mayor_for([1]) == "El elemento mayor es 1"
    assert mayor_for([1, 2]) == "El elemento mayor es 2"
    assert mayor_for([2, 1]) == "El elemento mayor es 2"
    assert mayor_for([2, 1, 3]) == "El elemento mayor es 3"

# Escriba una funcion llamada segundo_mayor que, dada una lista de numeros, retorne el segundo numero
# mas grande presente en la misma. Si la lista esta vacia o no tiene al menos dos elementos distintos
# la funcion debe indicar esta situacion 

def segundo_mayor(lista):
    lista.sort()

    if lista == []:
        return "Lista vacia"
    
    if len(lista) < 2:
        return "Elementos insuficientes"
    
    if len(lista) == 2 and lista[0] == lista[1]:
        return "No hay elementos diferentes"
    
    mayor = lista[0]
    segundo_mayor = lista[0]

    for indice in range(0, len(lista)):
        if lista[indice] > mayor:
            segundo_mayor = mayor
            mayor = lista[indice]

    return "El segundo elemento mayor es " + str(segundo_mayor)

def test_segundo_mayor():
    assert segundo_mayor([]) == "Lista vacia"
    assert segundo_mayor([1]) == "Elementos insuficientes"
    assert segundo_mayor([1, 1]) == "No hay elementos diferentes"
    assert segundo_mayor([1, 2]) == "El segundo elemento mayor es 1"
    assert segundo_mayor([1, 2, 3]) == "El segundo elemento mayor es 2"
    assert segundo_mayor([3, 2, 1]) == "El segundo elemento mayor es 2"
    assert segundo_mayor([3, 2, 2]) == "El segundo elemento mayor es 2"
    assert segundo_mayor([3, 2, 3]) == "El segundo elemento mayor es 2"

# Escriba una funcion llamada n_mayor que reciba una lista de numeros y un numero natural n.
# El objetivo de la funcion es retornar el n-esimo mayor elemento de la lista. Si la lista no 
# contiene n elementos distintos, la funcion debe indicar esta situacion.

def n_mayor(lista, n):
    
    if lista == []:
        return "Lista vacia"
    
    if len(lista) < n:
        return "Elementos insuficientes"
    
    mayor = lista[0]
    indice = 1

    while n > 0:
        if lista[indice] > mayor:
            mayor = lista[indice]
            n -= 1
        indice += 1

    return "El elemento mayor es " + str(mayor)

def test_n_mayor():
    assert n_mayor([], 1) == "Lista vacia"
    assert n_mayor([1], 2) == "Elementos insuficientes"
    assert n_mayor([1, 2, 3, 4, 5], 3) == "El elemento mayor es 4"
    assert n_mayor([1, 2, 3], 1) == "El elemento mayor es 2"
    assert n_mayor([3, 2, 1, 4, 5], 1) == "El elemento mayor es 4"

# Es posible hacer una version recursiva de la funcion n_mayor? Si lo es, escribala. 
# Es caso de no serlo, explique porque

def n_mayor_recursiva(lista, n, indice = 0, mayor = 0):
    
    if lista == []:
        return "Lista vacia"
    
    if len(lista) < n:
        return "Elementos insuficientes"
    
    if n == 0:
        return "El elemento mayor es " + str(mayor)
    
    if n > 0:
        if lista[indice] > mayor:
            return n_mayor_recursiva(lista, n - 1, indice + 1, mayor = lista[indice])
        
        return n_mayor_recursiva(lista, n, indice + 1, mayor)    

def test_n_mayor_recursiva():
    assert n_mayor_recursiva([], 1) == "Lista vacia"
    assert n_mayor_recursiva([1], 2) == "Elementos insuficientes"
    assert n_mayor_recursiva([1, 2, 3, 4, 5], 3) == "El elemento mayor es 3"
    assert n_mayor_recursiva([1, 2, 3], 1) == "El elemento mayor es 1"
    assert n_mayor_recursiva([3, 2, 1, 4, 5], 1) == "El elemento mayor es 3"

