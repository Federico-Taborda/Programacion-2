import subprocess
from math import *

# Se representa al laberinto como un diccionario que contiene las configuraciones del laberinto
# Se representa a la dimension del laberinto como un numero entero positivo
# Se representa a cada casilla del laberinto como una tupla de dos enteros positivos (x, y)
# Se representa como esta formado el laberinto como una matriz de listas de caracteres

# Dada la salida del programa en C la funcion generara una matriz de listas de caracteres
def generarMatriz():
    resultado = subprocess.run(["./a.out", "EntradaLaberinto.txt"], capture_output=True, text=True)
    salida = resultado.stdout
    laberinto = []
    fila = []

    for caracter in salida:
        if caracter != "\n":
            fila.append(caracter)

        if caracter == "\n":
            laberinto.append(fila)
            fila = []

    #print(salida)
    
    return laberinto

# Dada una matriz y un caracter la funcion devuelve una tupla de dos enteros (x, y)
# que representa las coordenadas de la casilla que coincide con el caracter
def obtenerCasilla(matriz, caracter):
    posX = 0
    posY = 0
    dimension = len(matriz)

    for x in range(0, dimension):
        for y in range(0, dimension):
            if matriz[x][y] == caracter:
                posX = x
                posY = y
    
    return (posX, posY)

# Inicializa un diccionario con los datos del laberinto
def inicializarLaberinto():
    matriz = generarMatriz()

    laberinto = { 
        "matriz": matriz,
        "dimension": len(matriz),
        "casillaSalida": obtenerCasilla(matriz, "|"),
        "casillaLlegada": obtenerCasilla(matriz, "X"),
    }

    return laberinto

# Dada una tupla de dos enteros (x, y) y una dimension de la matriz la funcion
# devuelve verdadero o falso si la casilla dada esta dentro de los limites del laberinto
def limiteLaberinto(casilla, dimension):
   (x, y) = casilla
   return x >= 0 and x < dimension and y >= 0 and y < dimension

# Dada una matriz y una casilla la funcion devuelve 
# verdadero o falso si la casilla dada es una pared o no
def esPared(matriz, casilla):
    (x, y) = casilla
    return matriz[x][y] == "1"

# Dadas dos casillas la funcion devuelve la distancia entre ambas
def obtenerDistancia(casillaUno, casillaDos):
    (x1, y1) = casillaUno
    (x2, y2) = casillaDos
    return sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

# Dado un laberinto y una casilla devuelve un conjunto de coordenadas de posibles movimientos
def generarPosiblesMovimientos(laberinto, casilla):
    (x, y) = casilla

    # Movimientos legales: Arriba, abajo, izquierda, derecha
    movimientosLegales = {(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)}
    # Movimientos ilegales: pared, fuera de la dimension
    movimientosIlegales = set()

    for casilla in movimientosLegales:
        if not limiteLaberinto(casilla, laberinto["dimension"]) or esPared(laberinto["matriz"], casilla):
            movimientosIlegales.add(casilla)

    return movimientosLegales.difference(movimientosIlegales)

# Dada una casilla actual, una casilla final y un conjunto de movimientos la funcion 
# devolvera la casilla con distancia mas corta a la casilla final
def distanciaMasCorta(casillaActual, casillaFinal, movimientos):
    masCorta = casillaActual

    for casilla in movimientos:
        if obtenerDistancia(casilla, casillaFinal) < obtenerDistancia(casillaActual, casillaFinal):
            masCorta = casilla

    return masCorta

# Dado un laberinto la funcion devolvera una lista de tuplas (x,y) que representara el recorrido del laberinto
def generarRecorrido(laberinto):
    recorrido = [laberinto["casillaSalida"]]
    casillaActual = recorrido[0]
    casillasDescartadas = set()
    posiblesMovimentos = generarPosiblesMovimientos(laberinto, casillaActual)

    if len(posiblesMovimentos) == 0:
        return []

    # Mientras la distancia de la casilla actual a la casilla de llegada sea mayor a 0
    # y haya posibles movimientos se buscara un recorrido
    while obtenerDistancia(casillaActual, laberinto["casillaLlegada"]) > 0 and len(posiblesMovimentos) > 0:
        posiblesMovimentos = generarPosiblesMovimientos(laberinto, casillaActual)
        posiblesMovimentos.difference(casillasDescartadas)

        siguienteCasilla = distanciaMasCorta(casillaActual, laberinto["casillaLlegada"], posiblesMovimentos.difference(set(recorrido)))

        if casillaActual == siguienteCasilla:
            if not len(recorrido) == 1:
                casillasDescartadas.add(casillaActual)
                recorrido.pop()
            else:
                posibleCasillas = list(posiblesMovimentos.difference(set(recorrido)))
                recorrido.append(posibleCasillas[0])
        else:
            recorrido.append(siguienteCasilla)

        casillaActual = recorrido[len(recorrido) - 1]

    return recorrido

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