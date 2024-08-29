def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
        
    return True

def imprimir_primos(n):
    for i in range (0, n):
        if es_primo(i):
            print(i)

imprimir_primos(30)

