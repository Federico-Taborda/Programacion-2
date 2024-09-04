def imprimir_suma(n = 0):
    if(n > 50):
        return 0
    
    return n + imprimir_suma(n + 1)

# Recursion en cola
def imprimir_suma_dos(n = 0, acumulador = 0):
    if n > 50:
        return acumulador
    
    return imprimir_suma_dos(n + 1, acumulador + n)

# Funcion iterativa
def imprimir_suma_for():
    acumulador = 0

    for x in range(50):
        acumulador += x
    
    return acumulador

print(imprimir_suma())
print(imprimir_suma_dos())
print(imprimir_suma_for())

def test_imprimir_sumar():
    assert imprimir_suma(0) == 1275