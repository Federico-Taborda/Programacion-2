# Solucion iterativa
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

# Solucion recursiva
def numero_triangular_recursiva(n, acumulador = 0):
    if n == 0:
        return acumulador
    
    return numero_triangular_recursiva(n - 1, acumulador + n)

def imprimir_triangulares(n):
    for x in range(1, n + 1):
        print(x, "-", numero_triangular_recursiva(x))

#imprimir_triangulares(5)
imprimir_triangulares(996)
#imprimir_triangulares(10)

def test_numero_triangular():
    assert numero_triangular_for(1) == 1
    assert numero_triangular_for(2) == 3
    assert numero_triangular_for(3) == 6
    assert numero_triangular_for(4) == 10
    assert numero_triangular_for(5) == 15