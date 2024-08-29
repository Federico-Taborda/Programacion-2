def es_potencia_de_dos(n):
    for i in range(0, n):
        if 2 ** i == n:
            return True
        
    return False
        
def devolver_suma(n, m):
    suma = 0

    for i in range(n, m):
        if es_potencia_de_dos(i):
            suma += i
    
    return suma

print(devolver_suma(1, 10))