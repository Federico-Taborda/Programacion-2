from random import *

# Ejercicio A
def apariciones_palabra(cadena:str) -> dict:
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

def apariciones_palabra_split(cadena):
    if cadena == []:
        return {}
    
    diccionario = {}
    lista = cadena.split()

    for palabra in lista:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    return diccionario

# Ejercicio B
def cantidad_caracteres(cadena):
    if cadena == []:
        return {}
    
    diccionario = {}
    
    for caracter in cadena:
        if caracter not in diccionario:
            diccionario[caracter] = 1
        else:
            diccionario[caracter] += 1
    
    return diccionario

# Ejercicio C
def tirar_dados():
    dado_uno = randint(1, 6)
    dado_dos = randint(1, 6)

    return (dado_uno, dado_dos)

def contar_sumas(iteraciones):
    diccionario = {}

    for x in range(0, iteraciones + 1):
        (dado_uno, dado_dos) = tirar_dados()
        suma = dado_uno + dado_dos
        if suma not in diccionario:
            diccionario[suma] = 1
        else:
            diccionario[suma] += 1
    
    return diccionario