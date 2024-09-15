def es_potencia_de_dos_for(n):
    for i in range(0, n):
        if 2 ** i == n:
            print(i)
            return True
        
    return False

def es_potencia_de_dos_while(n):
    indice = 0
    es_potencia = 2 ** indice == n

    while not es_potencia and indice <= n:
        if 2 ** indice == n:
            es_potencia = True
        indice += 1

    return es_potencia

def es_potencia_de_dos_recursivo(n, indice = 0):
    if indice >= n:
        return False
    
    if 2 ** indice == n:
        return True
    
    return es_potencia_de_dos_recursivo(n, indice + 1)
        
def devolver_suma(n, m):
    suma = 0

    for i in range(n, m):
        if es_potencia_de_dos_while(i):
            print(i)
            suma += i
    
    return suma

def test_es_potencia():
    assert es_potencia_de_dos_for(2) and es_potencia_de_dos_while(2) and es_potencia_de_dos_recursivo(2) == True
    assert es_potencia_de_dos_for(64) == True
    assert es_potencia_de_dos_while(64) == True
    assert es_potencia_de_dos_recursivo(64) == True

def test_devolver_suma():
    assert devolver_suma(1, 10) == 15
    assert devolver_suma(2, 10) == 14
    assert devolver_suma(32, 33) == 32
    assert devolver_suma(32, 65) == 96