def imprimir_sumar(n):
    if(n == 0):
        return 0
    
    return n + imprimir_sumar(n - 1)

#Recursion en cola
def imprimir_suma_dos(n = 0, acumulador = 0):
    if n == 0:
        return acumulador
    
    return imprimir_suma_dos(n - 1, acumulador + n)

#Funcion iterativa
def imprimir_suma_for(n):
    acumulador = 0

    for x in range(n + 1):
        acumulador += x
    
    return acumulador

print(imprimir_sumar(5))
print(imprimir_suma_dos(5))
print(imprimir_suma_for(5))

def test_imprimir_sumar():
    assert imprimir_sumar(0) == 0
    assert imprimir_sumar(1) == 1
    assert imprimir_sumar(5) == 15
    assert imprimir_sumar(10) == 55

def test_imprimir_sumar_dos():
    assert imprimir_suma_dos(0) == 0
    assert imprimir_suma_dos(1) == 1
    assert imprimir_suma_dos(5) == 15
    assert imprimir_suma_dos(10) == 55
    
def test_imprimir_sumar_for():
    assert imprimir_suma_for(0) == 0
    assert imprimir_suma_for(1) == 1
    assert imprimir_suma_for(5) == 15
    assert imprimir_suma_for(10) == 55