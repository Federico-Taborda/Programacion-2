def imprimir_suma(n = 0):
    if(n > 50):
        return 0
    
    return n + imprimir_suma(n + 1)

def imprimir_suma_dos(n = 0, acumulador = 0):
    if n > 50:
        return acumulador
    
    return imprimir_suma_dos(n + 1, acumulador + n)

def imprimir_suma_for():
    acumulador = 0

    for x in range(50):
        acumulador += x
    
    return acumulador
