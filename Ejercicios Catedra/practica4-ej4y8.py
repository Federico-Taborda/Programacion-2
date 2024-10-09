
# Ejercicio 4
def agrupar(lista):
    resultado = {}
    for clave, valor in lista:
        if clave in resultado:
            resultado[clave].append(valor)
        else:
            resultado[clave] = [valor]
    return resultado


# Ejercicio 8
import random

def reemplazaSinonimos(texto, sinonimos):
    palabras = texto.split()
    resultado = []
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in sinonimos:
            sinonimosDePalabra = sinonimos[palabra]
        else:
            sinonimosDePalabra = []
        sinonimo = buscarSinonimo(palabra, sinonimosDePalabra)
        resultado.append(sinonimo)
    nuevaFrase = " ".join(resultado)
    return nuevaFrase.capitalize() # "hola como estas" -> "Hola como estas"

def buscarSinonimo(palabra, sinonimos):
    if sinonimos != []:
        i = random.randrange(0, len(sinonimos))
        return sinonimos[i]
    else:
        return palabra



sinonimos = {"lindo":["hermoso", "bello", "precioso"], "hola": ["buen dia", "buenas tardes"], "adios": ["chau", "hasta luego"], "bar": ["restaurante", "pub", "bodegon"], "comer": ["cenar", "morfar"]}
frase = "Hola que lindo dia hace hoy y que lindo bar elegiste para comer"

# Ejercicio 9
def valorCarrito(precios, carrito):
    valorTotal = 0
    for prod, cant in carrito.items():
        if prod not in precios:
            print("El carrito es invalido. Tiene un producto no disponible: " + prod)
            return -1
        valorTotal += precios[prod] * cant
    return valorTotal
