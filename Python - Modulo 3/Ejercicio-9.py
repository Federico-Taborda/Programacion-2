def mostrar_caracteres(palabra):
    if palabra == palabra[0]:
        return print(palabra)

    print(palabra[-1])
    return mostrar_caracteres(palabra[:-1])

#mostrar_caracteres("hola")

def mostrar_caracteres_recursivo(palabra, index = -1):
    if abs(index) == len(palabra):
        return print(palabra[index])
    
    print(palabra[index])
    return mostrar_caracteres_recursivo(palabra, index - 1)

mostrar_caracteres_recursivo("hola")