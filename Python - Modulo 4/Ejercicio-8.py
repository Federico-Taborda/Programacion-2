from random import *

def sinonimizar(texto:str, sinonimos:list) -> str:
    lista_palabras = texto.split()
    nuevo_texto = ""
        
    for palabra in lista_palabras:
        if palabra in sinonimos:
            lista = sinonimos[palabra]
            indice = randint(0, len(lista) - 1);
            nuevo_texto += lista[indice]
        else:
            nuevo_texto += palabra

        nuevo_texto += " "

    return nuevo_texto

cadena = "la lluvia caia en el campo "
sinonimos = {
    "lluvia": ["precipitacion", "tormenta"],
    "campo": ["terreno", "suelo"],
}

print(sinonimizar(cadena, sinonimos))