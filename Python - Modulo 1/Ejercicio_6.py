def imprimir_suma(n, m):
    numero = n + 1
    
    if(numero >= m):
        return 0
    
    return numero + imprimir_suma(n + 1, m)

def imprimir_suma_dos(n, m, acumulador = 0):
    if n + 1 >= m:
        return acumulador
    
    acumulador += n + 1

    return imprimir_suma_dos(n + 1, m, acumulador)

def imprimir_suma_for(n, m):
    acumulador = 0

    for x in range(n + 1, m):
        acumulador += x

    return acumulador

