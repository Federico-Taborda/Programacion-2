def imprimir_suma(n, m):
    numero = n + 1
    
    if(numero >= m):
        return 0
    
    return numero + imprimir_suma(n + 1, m)

# Recursion en cola
def imprimir_suma_dos(n, m, acumulador = 0):
    if n + 1 >= m:
        return acumulador
    
    acumulador += n + 1

    return imprimir_suma_dos(n + 1, m, acumulador)

# Funcion iterativa
def imprimir_suma_for(n, m):
    acumulador = 0

    for x in range(n + 1, m):
        acumulador += x

    return acumulador
    
print(imprimir_suma(1, 4))
print(imprimir_suma_dos(1, 4))
print(imprimir_suma_for(1, 4))

def test_imprimir_suma():
    assert imprimir_suma(1, 4) == 5
    assert imprimir_suma(0, 4) == 6
    assert imprimir_suma(0, 1) == 0
    assert imprimir_suma(0, 0) == 0

def test_imprimir_suma_dos():
    assert imprimir_suma_dos(1, 4) == 5
    assert imprimir_suma_dos(0, 4) == 6
    assert imprimir_suma_dos(0, 1) == 0
    assert imprimir_suma_dos(0, 0) == 0

def test_imprimir_suma_for():
    assert imprimir_suma_for(1, 4) == 5
    assert imprimir_suma_for(0, 4) == 6
    assert imprimir_suma_for(0, 1) == 0
    assert imprimir_suma_for(0, 0) == 0

