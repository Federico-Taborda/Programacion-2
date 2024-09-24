def apariciones_palabra(cadena):
    diccionario = {}
    palabra = ""
    indice = 0

    for caracter in cadena:
        if caracter != " ":
            palabra += caracter

        if caracter == " " or indice == len(cadena) - 1:
            if palabra in diccionario:
                diccionario[palabra] += 1
            else:
                diccionario[palabra] = 1

            palabra = ""
        
        indice += 1
    
    return diccionario

print(apariciones_palabra("que que tal que tal"))