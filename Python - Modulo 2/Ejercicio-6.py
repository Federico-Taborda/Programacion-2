def numero_triangular(n):
    triangular = 0
    for x in range(1, n + 1):
        triangular += x
    
    return triangular

def test_numero_triangular():
    assert numero_triangular(1) == 1
    assert numero_triangular(2) == 3
    assert numero_triangular(3) == 6
    assert numero_triangular(4) == 10
    assert numero_triangular(5) == 15

def imprimir_triangulares(n):
    for x in range(1, n + 1):
        print(numero_triangular(x))

imprimir_triangulares(5)