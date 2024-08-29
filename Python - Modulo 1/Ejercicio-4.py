def imprimir_sumar(n):
    if(n > 50):
        return 0
    else:
        return n + imprimir_sumar(n + 1)
    
print(imprimir_sumar(0))

def test_imprimir_sumar():
    assert imprimir_sumar(0) == 1275
    
