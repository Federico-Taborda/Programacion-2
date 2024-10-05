def lista_a_diccionario(lista:list) -> dict:
    diccionario = {}

    for (clave, valor) in lista:
        if clave in diccionario:
            diccionario[clave].append(valor)
        else:
            diccionario[clave] = [valor]

    return diccionario

print(lista_a_diccionario([("Hola", "don pepito"), ("Hola", "don jose"), ("Buenos", "dias")]))