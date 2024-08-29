from random import *

def lanzar_dado():
    contador = 0
    numero = randint(1, 6)

    while not numero == 6:
        print(numero)
        contador += 1
        numero = randint(1, 6)

    return print("Cantidad de lanzamientos:", contador)

#lanzar_dado()

def lanzar_dados(n):
    lanzamientos = 0
    contador = 0
    primer_dado = 1
    segundo_dado = 1

    while not lanzamientos == n:
        lanzamientos += 1
        primer_dado = randint(1, 6)
        segundo_dado = randint(1, 6)

        if primer_dado == segundo_dado: 
            contador += 1
            print(primer_dado, segundo_dado)

    return print("Lanzamientos iguales:", contador)

#lanzar_dados(1000)

def juego_de_dados(n):
    lanzamientos = 0
    ganancias = 0
    dado = 0

    while not lanzamientos == n:
        lanzamientos += 1
        dado = randint(1, 6)

        if dado == 6: 
            ganancias += 4
        elif dado == 3:
            ganancias += 1
        elif dado == 1:
            continue
        else:
            ganancias -= 2
        print("Valor:", dado, "Pozo:",ganancias)
    
    return ganancias

#juego_de_dados(100)