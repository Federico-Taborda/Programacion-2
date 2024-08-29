def elimina_uno(lista):
    nueva_lista = []
    for i in range(1, len(lista) - 1):
        nueva_lista.append(lista[i])
    
    return nueva_lista

def elimina_dos(lista): 
    return lista[1:len(lista) - 1]

print(elimina_uno(["a", "b", "c", "d"]))
print(elimina_dos(["a", "b", "c", "d"]))
