import random

def tomar_carta() -> tuple:
    cartas = [ "picas", "trebol", "diamantes", "corazones" ]
    numero = random.randint(1, 13)
    carta = random.randint(0, 3)

    carta_tomada = cartas[carta]

    if numero == 1: return ("As ", carta_tomada)
    if numero == 11: return ("J", carta_tomada)
    if numero == 12: return ("Q", carta_tomada)
    if numero == 13: return ("K", carta_tomada)
    
    return (numero, carta_tomada)

def contar_repeticiones(mano:list) -> bool:
    for carta in mano:
        repeticiones = 0    
        for otra_carta in mano:
            if carta[0] == otra_carta[0]:
                repeticiones += 1
        
        if repeticiones >= 4:
            return True
    
    return False

def poker():
    mano = []

    while len(mano) < 5:
        carta = tomar_carta()
        if carta not in mano:
            mano.append(carta)
    
    return contar_repeticiones(mano)

#for x in range(10000):
    #poker()