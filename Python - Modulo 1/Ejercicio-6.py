def imprimir_suma(n, m):
    numero = n + 1
    
    if(numero >= m):
        return 0
    
    return numero + imprimir_suma(n + 1, m)
    
print(imprimir_suma(1, 4))

def test_imprimir_suma():
    assert imprimir_suma(1, 4) == 5
    assert imprimir_suma(0, 4) == 6
    assert imprimir_suma(0, 1) == 0
    assert imprimir_suma(0, 0) == 0

