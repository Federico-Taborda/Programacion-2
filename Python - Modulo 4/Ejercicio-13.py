def mayor(lista):
    mayor = lista[0]

    for n in range(1, len(lista)):
        if lista[n] > mayor:
            mayor = lista[n]

    return mayor

def lista_menores(lista_desordenada):
    max = mayor(lista_desordenada)
    conjunto = set()

    for numero in range(0, max):
        if numero not in set(lista_desordenada):
            conjunto.add(numero)
    
    return conjunto

#print(lista_menores([4, 7 ,2, 9, 4, 7, 1]))