# Se representa al tiempo como una tupla
# tiempo = (hora, minutos, segundo)

def suma_tiempo(tiempo_uno:tuple, tiempo_dos:tuple) -> tuple:
    horas = tiempo_uno[0] + tiempo_dos[0]
    minutos = tiempo_uno[1] + tiempo_dos[1]
    segundos = tiempo_uno[2] + tiempo_dos[2]

    if segundos > 59:
        segundos -= 60
        minutos += 1
    
    if minutos > 59:
        minutos -= 60
        horas += 1

    return (horas, minutos, segundos)