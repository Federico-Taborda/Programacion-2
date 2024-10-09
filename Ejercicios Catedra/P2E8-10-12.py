from math import *

def ingreso_notas_():
    seguir    = True
    sumaNotas = 0
    cantNotas = 0

    while(seguir):
        nota = float(input("Ingresar una nota: "))
        sumaNotas = sumaNotas + nota
        cantNotas = cantNotas + 1
        continuar = input("Quiere continuar?[s/n]: ")
        if not "s" == continuar.lower():
            seguir = False
    return sumaNotas / cantNotas


def ingreso_notas():
    seguir    = True
    sumaNotas = 0
    cantNotas = 0

    while seguir:
        nota = float(input("Ingresar una nota: "))
        
        sumaNotas += nota
        cantNotas += 1
        
        continuar = input("Quiere continuar?[s/n]: ")
        
        seguir = "s" == continuar.lower()
    
    return sumaNotas / cantNotas


# print("El promedio de tus notas es: ", ingreso_notas())

# Ejercicio 10

def multiplos_for (n, m):
    cant_multiplos = 0
    for i in range(n, m):
        if i % n == 0:
            cant_multiplos += 1
    return cant_multiplos


def multiplos_while (n, m):
    cant_multiplos = 0
    multiplo = n * (cant_multiplos + 1)
    while multiplo < m:
        cant_multiplos += 1
        multiplo = n * (cant_multiplos + 1)
    return cant_multiplos

# Ejercicio 12

def primos_hasta(n):
    primos = []
    for p in range(n+1):
        if es_primo4(p):
            primos.append(p)
    return primos

def es_primo1(p):
    if p <= 1:
        return False

    cantidad_de_divisores = 0
    for d in range(1, p+1):
        if p % d == 0:
            cantidad_de_divisores += 1

    return cantidad_de_divisores == 2

def es_primo2(p):
    if p <= 1:
        return False

    cantidad_de_divisores = 0
    for d in range(2, p):
        if p % d == 0:
            cantidad_de_divisores += 1

    return cantidad_de_divisores == 0

def es_primo3(p):
    if p <= 1:
        return False

    cantidad_de_divisores = 0
    for d in range(2, int(sqrt(p))+1):
        if p % d == 0:
            cantidad_de_divisores += 1

    return cantidad_de_divisores == 0

def es_primo4(p):
    if p <= 1:
        return False

    if p % 2 == 0:
        return p == 2

    cantidad_de_divisores = 0
    for d in range(3, int(sqrt(p))+1, 2):
        if p % d == 0:
            cantidad_de_divisores += 1

    return cantidad_de_divisores == 0

def primos_hasta_criba(n):

    cantidad_de_divisores = [0] * (n+1)
    for p in range(1, n+1):
        for m in range(p, n+1, p):
            cantidad_de_divisores[m] += 1
    
    primos = []
    for p in range(n+1):
        if p > 1 and cantidad_de_divisores[p] == 2:
            primos.append(p)

    return primos

def primos_hasta_criba_opt(n):

    criba = [True] * (n+1)
    for p in range(2, n+1):
        if criba[p]:
            for m in range(p*p, n+1, p):
                criba[m] = False
    
    primos = []
    for p in range(n+1):
        if p > 1 and criba[p]:
            primos.append(p)

    return primos

print(len(primos_hasta_criba_opt(100000)))
