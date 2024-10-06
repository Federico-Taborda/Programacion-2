# Dado un numero n la funcion devolvera el factorial de n
def factorial(n:int) -> int:
    if n == 0:
        return 1
    
    return n * factorial(n - 1)

def mostrar_factorial():
    numero = input("Ingrese un numero: ")

    if not numero.isnumeric():
        print("Solo se puede ingresar numeros")
        return mostrar_factorial()

    print(factorial(int(numero)))
    return mostrar_factorial()

#mostrar_factorial()
