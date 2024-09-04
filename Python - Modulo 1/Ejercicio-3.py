# Recursion en cola
def imprimir_recursivo(n, m):
    if n == 0:
        return m
    
    if m % 2 == 0:
        print(m)
        return imprimir_recursivo(n - 1, m + 1)
     
    return imprimir_recursivo(n, m + 1)

# Funcion iterativa
def imprimir_for(n, m):
    for x in range(n):
        if m % 2 == 0:
            print(m)
            m += 1

        m += 1


def imprimir_iterativo(n, m):
    
    while n > 0:
        if m % 2 == 0:
            print(m)
            n -= 1
            m += 1
        
        m += 1
    
    return m

imprimir_recursivo(5, 10)
imprimir_for(5, 10)
imprimir_iterativo(6, 10)