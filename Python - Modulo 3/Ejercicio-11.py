def contar_vocales(cadena:str) -> any:
    vocales = ["a", "e", "i", "o", "u"]
    contadores = [0, 0, 0, 0, 0]

    for x in cadena:
        if x == vocales[0]:
            contadores[0] += 1
        elif x == vocales[1]:
            contadores[1] += 1
        elif x == vocales[2]:
            contadores[2] += 1
        elif x == vocales[3]:
            contadores[3] += 1
        elif x == vocales[4]:
            contadores[4] += 1

    return print(contadores[0], contadores[1] ,contadores[2] ,contadores[3] ,contadores[4])

contar_vocales("esto es una cadena")
