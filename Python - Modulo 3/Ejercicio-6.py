def elimina_duplicado(lista):
    nueva_lista = []

    for x in lista:
        if not x in nueva_lista:
            nueva_lista.append(x)
    
    return nueva_lista

print(elimina_duplicado(["a", "a", "b"]))