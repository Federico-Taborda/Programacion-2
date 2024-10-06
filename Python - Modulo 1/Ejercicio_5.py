def imprimir_sumar(n:int) -> int:
    if(n == 0):
        return 0
    
    return n + imprimir_sumar(n - 1)

def imprimir_suma_dos(n:int = 0, acumulador:int = 0) -> int:
    if n == 0:
        return acumulador
    
    return imprimir_suma_dos(n - 1, acumulador + n)

def imprimir_suma_for(n:int) -> int:
    acumulador = 0

    for x in range(n + 1):
        acumulador += x
    
    return acumulador