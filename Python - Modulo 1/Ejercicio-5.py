def imprimir_sumar(n):
    if(n == 0):
        return 0
    
    return n + imprimir_sumar(n - 1)
    
print(imprimir_sumar(5))

def test_imprimir_sumar():
    assert imprimir_sumar(0) == 0
    assert imprimir_sumar(1) == 1
    assert imprimir_sumar(5) == 15
    assert imprimir_sumar(10) == 55
    
