def acumular(lista):
    nueva_lista = [lista[0]]
    
    for i in range(1, len(lista)):
        elemento_anterior =  nueva_lista[len(nueva_lista) - 1]
        nueva_lista.append(lista[i] + elemento_anterior)

    return nueva_lista

print(acumular([1, 2, 3]))
