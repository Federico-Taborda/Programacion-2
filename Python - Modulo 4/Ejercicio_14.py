def dias_disponible(nombres:dict) -> set:
    disponibles = set()

    for persona in nombres:
        dias_persona = set(nombres[persona])

        if disponibles == set():
            disponibles |= dias_persona
        disponibles &= dias_persona
    
    return set(disponibles)

# Solucion de la clase practica
def ej14(dict):
    a = set(range(1,31))
    for element in dict:
        b = set(dict[element])
        a = a.intersection(b)
    
    return a