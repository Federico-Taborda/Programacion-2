def caracter_palabra(cadena:str) -> dict:
    if cadena == "":
        return {}

    diccionario = {}
    lista_palabras = cadena.split()

    for palabra in lista_palabras:
        for letra in palabra:
            if letra not in diccionario:
                diccionario[letra] = ""
                
            if len(diccionario[letra]) < len(palabra):
                diccionario[letra] = palabra
    
    return diccionario