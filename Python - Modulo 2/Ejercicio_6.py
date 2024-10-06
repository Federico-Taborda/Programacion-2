def numero_triangular_for(n):
    triangular = 0
    for x in range(1, n + 1):
        triangular += x
    
    return triangular

def numero_triangular_while(n):
    triangular = 0
    while n > 0:
        triangular += n
        n -= 1

    return triangular

def numero_triangular_recursiva(n, acumulador = 0):
    if n == 0:
        return acumulador
    
    return numero_triangular_recursiva(n - 1, acumulador + n)

def imprimir_triangulares(n):
    for x in range(1, n + 1):
        print(x, "-", numero_triangular_recursiva(x))