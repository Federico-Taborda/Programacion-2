# Barco

# Las coordenadas de cada seccion del barco se representan como una tupla de dos componentes
# donde cada componente seran de tipo number representando la posicion x e y de la coordenada
# de una seccion del barco

# Representamos un barco como un objeto con dos claves
# coordenadas: un conjunto de coordenadas 
# impactos: un conjunto de coordenadas inicializado vacio

# Disparo

# Representamos un disparo como una tupla de dos componentes donde cada componente
# sera de tipo number representando la posicion x e y de la coordenada del disparo

# Tablero

# Representamos las casillas del tablero como una tupla de dos componentes
# donde cada componente seran de tipo number representando la posicion x e y de la coordenada
# de cada casilla

# Representamos el tablero como un objeto con tres claves
# coordenadas: un conjunto de coordenadas inicializado con todas las coordenadas
# barcos: una lista de barcos inicializada vacia
# disparos: un conjunto de disparos realizados


tablero = {
    'coordenadas': {(1,1), (1,2), (1,3), (1,4),
                    (2,1), (2,2), (2,3), (2,4),
                    (3,1), (3,2), (3,3), (3,4),
                    (4,1), (4,2), (4,3), (4,4),
                },
    'barcos': [{
    'coordenadas': {(3,1), (3,2), (3,3)},
    'impactos': set(),
    'disparos': set()
}]
}

barco = {
    'coordenadas': {(1,1), (1,2), (1,3)},
    'impactos': set()
}

def agregarBarco(tablero, barcoIngresado):
    dentro_del_limite = 0
    casillas_disponibles = 0

    for coordenada in barcoIngresado['coordenadas']:
        # Verifica si las coordenadas estan dentro de los limites del tablero
        if coordenada in tablero['coordenadas']:
            dentro_del_limite += 1
        # Verifica si las coordenadas no estan utilizadas por otros barcos
        if len(tablero['barcos']) >= 1:
            for barco in tablero['barcos']:
                if coordenada not in barco['coordenadas']:
                    casillas_disponibles += 1

    # Si todas las casillas estan dentro de los limites y estan disponibles se agregara el barco al tablero
    if(dentro_del_limite == len(barcoIngresado['coordenadas']) and casillas_disponibles == len(barcoIngresado['coordenadas'])):
        tablero['barcos'].append(barcoIngresado)
        return tablero

    return tablero

def disparo(tablero, disparo):
    if disparo not in tablero['coordenadas'] or disparo in tablero['disparos']:
        return (tablero, "DISPARO NO VALIDO")
    
    accion = "AGUA"
    tablero['disparos'].append(disparo)

    for barco in tablero['barcos']:
        if disparo in barco['coordenadas']:
            accion = "TOCADO"
            barco['impactos'].add(disparo)

            if len(barco['coordenadas']) == len(barco['impactos']):
                accion = "HUNDIDO"

    return (tablero, accion)

def juegoTerminado(tablero):
    hundidos = 0
    for barco in tablero['barcos']:
        if len(barco['coordenadas']) == len(barco['impactos']):
            hundidos += 1
    
    return len(tablero['barcos']) == hundidos