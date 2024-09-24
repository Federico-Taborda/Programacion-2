def caracter_palabra(cadena):
    if cadena == "":
        return {}

    diccionario = {}
    
    for letra in cadena:
        if letra != " ":
            if letra not in diccionario:
                diccionario[letra] = ""
            
    lista_palabras = cadena.split()

    for palabra in lista_palabras:
        for letra in palabra:
            if len(diccionario[letra]) < len(palabra):
                diccionario[letra] = palabra
    
    return diccionario
    
print(caracter_palabra("la letra en la palabra mas larga"))