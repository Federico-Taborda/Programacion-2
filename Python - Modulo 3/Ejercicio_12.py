def contar_palabras_for(cadena:str) -> int:
    palabra = ""
    contador = 0

    for x in range(0, len(cadena)):
        if cadena[x] != " ":
            palabra += cadena[x]

        else:
            if len(palabra) > 5:
                contador += 1 
            palabra = ""

    return contador
