def cantidad_elementos_distintos(lista:list) -> int:
    nueva_lista = []

    for x in lista:
        if not x in nueva_lista:
            nueva_lista.append(x)
    
    return len(nueva_lista)

print(cantidad_elementos_distintos(["a", "a", "b"]))