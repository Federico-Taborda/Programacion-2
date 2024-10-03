def dias_disponible(nombres):
    disponibles = set()

    for persona in nombres:
        dias_persona = set(nombres[persona])

        if disponibles == set():
            disponibles |= dias_persona
        disponibles &= dias_persona
    
    return set(disponibles)

lista_nombres = {
    "a": ["Lun", "Mar", "Jue", "Vie"],
    "b": ["Jue", "Vie"],
    "c": ["Mar", "Jue"],
    "d": ["Jue", "Vie", "Sab", "Dom"]
}

print(dias_disponible(lista_nombres))

def ej14(dict):
    a = set(range(1,31))
    for element in dict:
        b = set(dict[element])
        a = a.intersection(b)
    
    return a