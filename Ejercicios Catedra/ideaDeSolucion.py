tablero = {
    "barcos": [
        ({(1,1), (1,2)}, 1, "horizontal")
    ],
    "barcos_vivos": 1,
    "ocupadas": {
        (1,1), (1,2)
    },
    "disparos": {
        (2,2), (1,1)
    }
}

def crear_barco(casilla, largo, orientacion):
    pass

def orientacion(barco):
    return barco[2]

def disparo(tablero, tiro):
    if not adentro(tablero, tiro) or disparo_repetido(tablero, tiro):
        return "invalido"
    elif barco_tocado(tablero, tiro):
        return "tocado"
    else:
        return "agua"

def disparo(tablero, tiro):
    if tiro in tablero["disparos"]:
        return "invalido"
    elif tiro in tablero["ocupadas"]:
        tablero["disparos"].add(tiro)

        i = 0
        encontrado = False
        hundido = False
        barcos = tablero["barcos"]
        while i < len(barcos) and not encontrado:
            posiciones, vidas, _ = barcos[i]
            if tiro in posiciones:
                encontrado = True
                barcos[i] = (posiciones, vidas-1)
                if vidas == 1:
                    tablero["barcos_vivos"] -= 1
                    hundido = True
            i += 1

        return "hundido" if hundido else "tocado"
    else:
        tablero["disparos"].add(tiro)
        return "agua"

# Ejercicio 3
def termino(tablero):
    return tablero["barcos"] == 0
