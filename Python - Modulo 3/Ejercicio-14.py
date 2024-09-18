# Se representa al tiempo como una tupla
# Donde el primer elemento es la hora
# El segundo los minutos
# Y el tercero los segundos
# tiempo = (hora, minutos, segundo)

def suma_tiempo(tiempo_uno, tiempo_dos):
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

def test_suma_tiempo():
    assert suma_tiempo((0,59,0), (0,0,60)) == (1,0,0)
    assert suma_tiempo((0,0,30), (0,0,30)) == (0,1,0)
    assert suma_tiempo((0,0,31), (0,0,30)) == (0,1,1)