# Hace mas operaciones porque itera uno por uno
def cantidad_multiplos_for(n:int, m:int) -> int:
    contador = 0

    for x in range(1, m):
        es_multiplo = x % n == 0
        es_menor = x < m

        if es_multiplo and es_menor:
            contador += 1

    return contador

#print(cantidad_multiplos_for(3, 30))
#print(cantidad_multiplos_for(7, 5000000))

# Esta es una opcion de mas simple de una lista de n a m haciendo saltos
# en multiplos de n
def cantidad_multiplos_for_dos(n:int, m:int) -> int:
    return len(range(n, m, n))

#print(cantidad_multiplos_for_dos(7, 5000000))

# Esta opcion es mejor porque van en saltos de n
def cantidad_multiplos_while(n:int, m:int) -> int:
    cantidad_multiplos = 0
    multiplo = 0

    while multiplo < m:
        cantidad_multiplos += 1
        multiplo += n 
    
    return cantidad_multiplos

#print(cantidad_multiplos_while(7, 5000000))