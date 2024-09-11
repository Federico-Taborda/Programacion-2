import math

def es_primo(num):
    divisores = 1
    primo = True

    while divisores < 2:
        for n in range(2, num + 1):
            if num % n == 0:
                divisores += 1

            if divisores > 2:
                primo = False
    
    return primo

def es_primo_dos(n):
    if n < 2:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def es_primo_tres(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def es_primo_cuatro(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def imprimir_primos(n):
    cantidad_primos = 0
    for i in range (2, n):
        if es_primo_tres(i):
            cantidad_primos += 1
            
    return cantidad_primos

#print(imprimir_primos(1000000))

def es_primo_cinco(n, primos):
    # Esta función retorna True si el número n es primo, usando la lista de primos generada por la criba
    return primos[n] if n < len(primos) else False

def criba_eratostenes(limite):
    # Genera una lista de booleanos donde True indica que el número es primo
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False  # 0 y 1 no son primos
    p = 2
    while p ** 2 <= limite:
        if primos[p]:
            for i in range(p * p, limite + 1, p):
                primos[i] = False  # Marca los múltiplos de p como no primos
        p += 1
    return primos

def imprimir_primos(n):
    # Usamos la criba de Eratóstenes para encontrar todos los primos hasta n
    primos = criba_eratostenes(n)
    
    # Contamos cuántos números son primos en el rango de 2 a n-1
    cantidad_primos = 0
    for i in range(2, n):
        if es_primo_cinco(i, primos):
            cantidad_primos += 1
            
    return cantidad_primos

print(imprimir_primos(10000000))  # Esto imprimirá cuántos números primos hay hasta n


