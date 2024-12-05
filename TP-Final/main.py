import subprocess
from math import *

def generarLaberinto():
    resultado = subprocess.run(["./a.out", "EntradaLaberinto.txt"], capture_output=True, text=True)
    salida = resultado.stdout
    laberinto = []
    fila = []

    for caracter in salida:
        if caracter != "\n":
            fila.append(caracter);

        if caracter == "\n":
            laberinto.append(fila)
            fila = []

    print(salida)
    
    return laberinto

# Devuelve una tupla que representa las coordenadas del punto
def obtenerCasilla(laberinto, caracter):
    posX = 0
    posY = 0

    for x in range(0, len(laberinto)):
        for y in range(0, len(laberinto[x])):
            if laberinto[x][y] == caracter:
                posX = x
                posY = y
    
    return (posX, posY)

# Devuelve un booleano que representa si la casilla dada esta dentro de los limites del laberinto
def limiteLaberinto(casilla, dimension):
   (x, y) = casilla
   return x >= 0 and x < dimension and y >= 0 and y < dimension
 
# Devuelve un booleano que representa si la casilla dada es una pared o no
def esPared(laberinto, casilla):
    (x, y) = casilla
    return laberinto[x][y] == "1"

# Dado un laberinto y una casilla devuelve un conjunto de coordenadas de posibles movimientos
def generarPosiblesMovimientos(laberinto, casilla):
    (x, y) = casilla
    movimientosLegales = {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}
    movimientosIlegales = set()

    for casilla in movimientosLegales:
        if not limiteLaberinto(casilla, laberinto["dimension"]) or esPared(laberinto["matriz"], casilla):
            movimientosIlegales.add(casilla)

    return movimientosLegales.difference(movimientosIlegales)

# Dadas dos casillas la funcion devuelve la distancia entre ambos
def obtenerDistancia(casillaUno, casillaDos):
    (x1, y1) = casillaUno
    (x2, y2) = casillaDos
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

# Dada una casilla actual, una casilla final y un conjunto de movimientos la funcion devolvera la casilla con distancia mas corta a la casilla final
def distanciaMasCorta(casillaActual, casillaFinal, movimientos):
    masCorta = casillaActual

    for casilla in movimientos:
        if obtenerDistancia(casilla, casillaFinal) < obtenerDistancia(casillaActual, casillaFinal):
            masCorta = casilla

    return masCorta

# Dado un laberinto la funcion devolvera una lista de tuplas que representara el recorrido del laberinto
def generarRecorrido(laberinto):
    recorrido = [laberinto["casillaSalida"]]
    casillaActual = recorrido[0]
    casillasDescartadas = set()
    posiblesMovimentos = generarPosiblesMovimientos(laberinto, casillaActual)

    if len(posiblesMovimentos) == 0:
        return []

    while obtenerDistancia(casillaActual, laberinto["casillaLlegada"]) != 0 and len(posiblesMovimentos) > 0:
        posiblesMovimentos = generarPosiblesMovimientos(laberinto, casillaActual)
        posiblesMovimentos.difference(casillasDescartadas)

        siguienteCasilla = distanciaMasCorta(casillaActual, laberinto["casillaLlegada"], posiblesMovimentos.difference(set(recorrido)))

        if casillaActual == siguienteCasilla:
            if not len(recorrido) == 1:
                casillasDescartadas.add(casillaActual)
                recorrido.pop()
            else:
                posibleCasillas = list(posiblesMovimentos)
                recorrido.append(posibleCasillas[0])
            
        else:
            casillaActual = siguienteCasilla
            recorrido.append(casillaActual)

        casillaActual = recorrido[len(recorrido) - 1]

    return recorrido

# Inicializa un diccionario con los datos del laberinto
def inicializarLaberinto():
    matriz = generarLaberinto()

    laberinto = { 
        "matriz": matriz,
        "dimension": len(matriz),
        "casillaSalida": obtenerCasilla(matriz, "|"),
        "casillaLlegada": obtenerCasilla(matriz, "X"),
    }

    return laberinto

def main():
    laberinto = inicializarLaberinto()
    recorrido = []

    # Mientras el recorrido sea una lista vacia se generara un nuevo laberinto
    while recorrido == []:
        laberinto = inicializarLaberinto()
        recorrido = generarRecorrido(laberinto)

    print(recorrido)

if __name__ == "__main__":
  main()