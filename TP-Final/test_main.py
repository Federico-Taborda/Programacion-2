from main import *

def test_obtenerDistancia():
    assert obtenerDistancia((0, 0), (3, 4)) == 5
    assert obtenerDistancia((1, 1), (1, 1)) == 0

def test_obtenerCasilla():
    matriz = [
        ["0", "0", "|"],
        ["0", "1", "0"],
        ["X", "0", "1"],
    ]
    assert obtenerCasilla(matriz, "|") == (0, 2)
    assert obtenerCasilla(matriz, "X") == (2, 0)

def test_limiteLaberinto():
    assert limiteLaberinto((0, 0), 3) == True
    assert limiteLaberinto((2, 2), 3) == True
    assert limiteLaberinto((3, 3), 3) == False
    assert limiteLaberinto((-1, 0), 3) == False
    assert limiteLaberinto((1, -1), 3) == False

def test_esPared():
    matriz = [
        ["0", "1", "0"],
        ["0", "1", "0"],
        ["X", "0", "1"],
    ]
    assert esPared(matriz, (0, 1)) == True
    assert esPared(matriz, (2, 0)) == False
    assert esPared(matriz, (1, 2)) == False

def test_obtenerDistancia():
    assert obtenerDistancia((0, 0), (3, 4)) == 5
    assert obtenerDistancia((1, 1), (1, 1)) == 0
    assert obtenerDistancia((2, 3), (5, 7)) == 5

def test_generarPosiblesMovimientos():
    laberinto = {
        "matriz": [
            ["0", "1", "0"],
            ["0", "1", "0"],
            ["X", "0", "1"],
        ],
        "dimension": 3,
    }
    movimientos = generarPosiblesMovimientos(laberinto, (1, 0))
    assert movimientos == {(0, 0), (2, 0)}