def elimina_uno(lista):
    nueva_lista = []
    for i in range(1, len(lista)):
        nueva_lista.append(lista[i])
    
    return nueva_lista

def elimina_dos(lista): 
    return lista[1:len(lista)]

# Esta opcion elimina el primer elemento de la lista fuera del ambito de la funcion
def elimina_tres(lista):
    del lista[0]
    return lista

# Esta opcion elimina el primer elemento de la lista dentro del ambito de la funcion
def elimina_cuatro(lista):
    nueva_lista = []
    nueva_lista += lista

    del nueva_lista[0]
    return nueva_lista

arr = ["a", "b", "c", "d"]
print(elimina_uno(arr))
print(elimina_dos(arr))
#print(elimina_tres(arr))
#print(elimina_cuatro(arr))

print(arr)
